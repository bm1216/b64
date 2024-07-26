import pytest
from encode import convert_to_b64


def test_convert_to_base64():
    test_cases = {
        "hello": "aGVsbG8=",
        "hi there my name is": "aGkgdGhlcmUgbXkgbmFtZSBpcw==",
    }
    for key, value in test_cases.items():
        result = convert_to_b64(key)
        assert (result) == value
