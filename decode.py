B64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


## To reverse the encoding method, we have to:
## 1. Convert the Base-64 string into a binary representation
## 2. Covnert the binary string to UTF-8
def convert_from_b64(encoded_string):
    i = 0
    binary_rep = ""
    while i < len(encoded_string):
        char = encoded_string[i]
        ## Padding is just a byte full of zeroes. Don't need to add rep for padding.
        if char == "=":
            # binary_rep += format(0, "06b")
            i += 1
            continue

        idx = B64.index(char)

        binary_rep += format(idx, "06b")
        i += 1

    ## Remove any additional padding that is added by the encoding.
    if len(binary_rep) % 8 != 0:
        binary_rep = binary_rep[: -(len(binary_rep) % 8)]
    ## We do this complex thing instead of just
    ## format("%x" % len(binary_rep, 2))
    ## because the above doesn't account for any leading zeros that might be present in the binary representation and just strips them.
    x = "{0:0{1}x}".format(int(binary_rep, 2), len(binary_rep) // 4)
    return bytes.fromhex(x).decode("utf-8")
