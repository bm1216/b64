import time
import encode
import decode
import base64

TEST_STRING = "\0\x01\x02\x03\x04\x05\x06\x07\b\t\n\x0B\f\r\x0E\x0F\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1A\x1B\x1C\x1D\x1E\x1F !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7F"

TEST_OUTPUT = "AAECAwQFBgcICQoLDA0ODxAREhMUFRYXGBkaGxwdHh8gISIjJCUmJygpKissLS4vMDEyMzQ1Njc4OTo7PD0+P0BBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWltcXV5fYGFiY2RlZmdoaWprbG1ub3BxcnN0dXZ3eHl6e3x9fn8="


def encode_compare():
    start = time.time()
    encode.convert_to_b64(TEST_STRING)
    print(
        "---- time taken for encoding in custom module %.10f seconds ------"
        % (time.time() - start)
    )

    start = time.time()
    base64.b64encode(TEST_STRING.encode("utf-8")).decode("utf-8")
    print(
        "---- time taken for encoding in python base64 %.10f seconds ------"
        % (time.time() - start)
    )


def decode_compare():
    start = time.time()
    decode.convert_from_b64(TEST_OUTPUT)
    print(
        "---- time taken for decoding in custom module %.10f seconds ------"
        % (time.time() - start)
    )

    start = time.time()
    base64.b64decode(TEST_OUTPUT).decode("utf-8")
    print(
        "---- time taken for decoding in python base64 %.10f seconds ------"
        % (time.time() - start)
    )


print("=======ENCODING=========")
encode_compare()

print("\n=======DECODING=========")
decode_compare()
