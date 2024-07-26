## b64

Sources used:

- https://en.wikipedia.org/wiki/Base64#Base64_table_from_RFC_4648
- https://www.rapidtables.com/code/text/ascii-table.html
- https://www.redhat.com/sysadmin/base64-encoding#:~:text=How%20Base64%20works,sysadmin's%20guide%20to%20Bash%20scripting.%20%5D

### Usage

```
> python main.py hello
aGVsbG8=
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

which is `SEVMTE8=`

