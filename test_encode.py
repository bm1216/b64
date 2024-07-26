import pytest
from encode import convert_to_b64


def test_convert_to_base64():
    data = "hello"
    result = convert_to_b64(data)
    assert (result) == "aGVsbG8="
