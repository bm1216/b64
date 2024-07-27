import pytest
from encode import convert_to_b64


def test_convert_to_base64():
    test_cases = {
        "hello": "aGVsbG8=",
        "hi there my name is": "aGkgdGhlcmUgbXkgbmFtZSBpcw==",
        "Lorem ipsum dolor sit amet, officia excepteur ex fugiat reprehenderit enim labore culpa sint ad nisi Lorem pariatur mollit ex esse exercitation amet. Nisi anim cupidatat excepteur officia. Reprehenderit nostrud nostrud ipsum Lorem est aliquip amet voluptate voluptate dolor minim nulla est proident. Nostrud officia pariatur ut officia. Sit irure elit esse ea nulla sunt ex occaecat reprehenderit commodo officia dolor Lorem duis laboris cupidatat officia voluptate. Culpa proident adipisicing id nulla nisi laboris ex in Lorem sunt duis officia eiusmod. Aliqua reprehenderit commodo ex non excepteur duis sunt velit enim. Voluptate laboris sint cupidatat ullamco ut ea consectetur et est culpa et culpa duis.": "TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIG9mZmljaWEgZXhjZXB0ZXVyIGV4IGZ1Z2lhdCByZXByZWhlbmRlcml0IGVuaW0gbGFib3JlIGN1bHBhIHNpbnQgYWQgbmlzaSBMb3JlbSBwYXJpYXR1ciBtb2xsaXQgZXggZXNzZSBleGVyY2l0YXRpb24gYW1ldC4gTmlzaSBhbmltIGN1cGlkYXRhdCBleGNlcHRldXIgb2ZmaWNpYS4gUmVwcmVoZW5kZXJpdCBub3N0cnVkIG5vc3RydWQgaXBzdW0gTG9yZW0gZXN0IGFsaXF1aXAgYW1ldCB2b2x1cHRhdGUgdm9sdXB0YXRlIGRvbG9yIG1pbmltIG51bGxhIGVzdCBwcm9pZGVudC4gTm9zdHJ1ZCBvZmZpY2lhIHBhcmlhdHVyIHV0IG9mZmljaWEuIFNpdCBpcnVyZSBlbGl0IGVzc2UgZWEgbnVsbGEgc3VudCBleCBvY2NhZWNhdCByZXByZWhlbmRlcml0IGNvbW1vZG8gb2ZmaWNpYSBkb2xvciBMb3JlbSBkdWlzIGxhYm9yaXMgY3VwaWRhdGF0IG9mZmljaWEgdm9sdXB0YXRlLiBDdWxwYSBwcm9pZGVudCBhZGlwaXNpY2luZyBpZCBudWxsYSBuaXNpIGxhYm9yaXMgZXggaW4gTG9yZW0gc3VudCBkdWlzIG9mZmljaWEgZWl1c21vZC4gQWxpcXVhIHJlcHJlaGVuZGVyaXQgY29tbW9kbyBleCBub24gZXhjZXB0ZXVyIGR1aXMgc3VudCB2ZWxpdCBlbmltLiBWb2x1cHRhdGUgbGFib3JpcyBzaW50IGN1cGlkYXRhdCB1bGxhbWNvIHV0IGVhIGNvbnNlY3RldHVyIGV0IGVzdCBjdWxwYSBldCBjdWxwYSBkdWlzLg==",
        "•": "4oCi",
        "℃ℓ℞testing℮•": "4oSD4oST4oSedGVzdGluZ+KEruKAog==",
    }
    for key, value in test_cases.items():
        result = convert_to_b64(key)
        assert (result) == value
