import sys
import encode


def main():
    output = encode.convert_to_b64(sys.argv[1])
    print(output)


if __name__ == "__main__":
    main()
