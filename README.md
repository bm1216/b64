## b64

This is my attempt at making a base64 encoder and decoder from scratch.

The difference between this and python's `base64` module is that mine works
natively with python `str`.

Sources used:

- https://en.wikipedia.org/wiki/Base64#Base64_table_from_RFC_4648
- https://www.rapidtables.com/code/text/ascii-table.html
- https://www.redhat.com/sysadmin/base64-encoding#:~:text=How%20Base64%20works,sysadmin's%20guide%20to%20Bash%20scripting.%20%5D
- https://docs.python.org/3/howto/unicode.html
- https://docs.python.org/3/library/string.html#string.Formatter
- https://datatracker.ietf.org/doc/html/rfc4648#section-4

### Usage

```
> python main.py hello
aGVsbG8=

> python main.py -d aGVsbG8=
hello
```

### Theory

Base-64 is an encoding system where data gets encoded into a 6-bit set of
characters (2^6 = 64). The characters are first coverted into 8 bits, and joined
together.

```
Example: HELLO
H = 01001000
E = 01000101
L = 01001100
L = 01001100
O = 01001111

010010001000101010011000100110001001111
```

Then, they are encoded starting from the left.

`010010|001000|101010|011000||100110|001001|111`

Base-64 encoding is done in 24 bit sequences, which is why additional padding is
added at the end to ensure we have 24 bits.

`010010|001000|101010|011000||100110|001001|111000|000000||`

which encodes to `SEVMTE8=`

This changes a little bit when we also have to account for strings encoded in
`UTF-8`. `UTF-8` represents characters as code-points, which are numbers between
0 and about 1.1 million.

- If the code point is < 128, it’s represented by the corresponding byte value.
  This way we can use a string of ASCII text as valid UTF-8 text.
- If the code point is >= 128, it’s turned into a sequence of two, three, or
  four bytes, where each byte of the sequence is between 128 and 255.

```
Example: ℈HELLO
℈ = \xe2\x84\x88 = 111000101000010010001000 (As you can see here, the character is encoded into 3 bytes)
H = 01001000
E = 01000101
L = 01001100
L = 01001100
O = 01001111

111000101000010010001000010010001000101010011000100110001001111
```

and the rest of the process is the same.
