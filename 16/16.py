from typing import Literal


input = "" 


def hex_to_binary(hex):
    return bin(int(hex, 16))[2:].zfill(len(hex) * 4)


def binary_to_dec(bin):
    if len(bin) > 0:
        return int(bin, 2)
    return 0


def parse_package(offset, bin_input):

    # Get all offsets
    version_offset = offset + 3
    type_id_offset = offset + 6
    length_type_id_offset = offset + 7

    # For solving
    versions.append(binary_to_dec(bin_input[offset:version_offset])) 


    # Use TYPE-ID to determine the package type
    type_id = binary_to_dec(bin_input[version_offset:type_id_offset])
    if type_id != 4:
        # Package is operator package
        length_type_id = binary_to_dec(bin_input[type_id_offset:length_type_id_offset])

        if length_type_id == 0:
            # next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
            sub_packet_len = binary_to_dec(bin_input[length_type_id_offset:length_type_id_offset+15])
            fixed = (length_type_id_offset+15)
            start = fixed

            while (start-fixed) < sub_packet_len:
                start = parse_package(start, bin_input)

            # Return current cursor pos for outer loop
            return start

        elif length_type_id == 1:
            # next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.
            packages_all = binary_to_dec(bin_input[length_type_id_offset:length_type_id_offset+11]) 
            packages_done = 0
            start = length_type_id_offset+11

            while packages_done != packages_all:
                start = parse_package(start, bin_input)
                packages_done += 1

            # Return current cursor pos for outer loop
            return start
            
    else:
        # package is a literal values
        start = type_id_offset
        stop = type_id_offset + 5
        
        bin_grp_val = ""
        while(True):
            bin_grp = bin_input[start:stop]
            if bin_grp[0] == "1":
                bin_grp_val += bin_grp[1:]
                start += 5
                stop += 5
                
            elif bin_grp[0] == "0":
                bin_grp_val += bin_grp[1:]
                literal_values.append(binary_to_dec(bin_grp_val))
                start += 5
                return start
            



versions = []
literal_values = []
# Convert hex input to binary
binary_input = hex_to_binary(input)

cursor = 0

while cursor < len(binary_input):
    # Parse input
    new_cursor = parse_package(cursor, binary_input)

    # Remaining chars are offset
    if sum([int(digit) for digit in list(binary_input[new_cursor:])]) == 0:
        break

    cursor += new_cursor

print(f"Solution: {sum(versions)}")
