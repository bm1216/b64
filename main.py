import sys
import time
import encode
import argparse
import decode
import base64


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("string")
    parser.add_argument(
        "-d",
        "--decode",
        help="Decode base64 string.",
        required=False,
        action="store_true",
    )
    args = parser.parse_args()
    if args.decode:
        print(decode.convert_from_b64(args.string))
    else:
        print(encode.convert_to_b64(args.string))


if __name__ == "__main__":
    main()
