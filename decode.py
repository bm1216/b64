B64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


## To reverse the encoding method, we have to:
## 1. Convert the Base-64 string into a binary representation
## 2. Covnert the binary string to UTF-8
def convert_from_b64(encoded_string):
    i = 0
    binary_rep = ""
    while i < len(encoded_string):
        char = encoded_string[i]
        ## Padding is just a byte full of zeroes
        if char == "=":
            binary_rep += format(0, "06b")
            i += 1
            continue

        idx = B64.index(char)

        binary_rep += format(idx, "06b")
        i += 1

    # print((binary_rep))
    x = format("%x" % int(binary_rep, 2))
    return bytes.fromhex(x).decode("utf-8").strip("\x00")
