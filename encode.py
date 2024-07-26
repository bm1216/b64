B64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


# Given a string, return the b64 output.
# We need to add up the binary representations of each character.
# b64 uses 24bit sequences. This means that padding needs to be added if it's not a  24bit sequence.
def convert_to_b64(string):
    binary = get_binary_representation(string)
    # print(binary)
    sequence = ""
    encoding = ""
    count = 0
    for bit in binary:
        sequence += bit
        count += 1
        if count == 24:
            encoding += get_24_bit_sequence(sequence)
            count = 0
            sequence = ""

    if 0 < count < 24:
        encoding += get_24_bit_sequence(sequence)

    return encoding


def get_24_bit_sequence(binary):
    cursor = 0
    track = ""
    b64encoding = ""
    for idx, value in enumerate(binary):
        track += value
        # print(track)
        cursor += 1
        # print(cursor)
        if cursor == 6:
            b64encoding += B64[int(track, 2)]
            cursor = 0
            track = ""

    if 0 < cursor < 6:
        b64encoding += B64[int(track, 2) << (6 - cursor)]

    # print(total)
    for _ in range(int((24 - len(binary)) / 6)):
        b64encoding += "="

    return b64encoding


def get_binary_representation(string):
    x = 0
    format_specifier = f"0{len(string)*8}b"
    for char in string:
        x <<= 8
        x |= ord(char) | 0x00000000

    return format(x, format_specifier)
