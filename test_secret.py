import os

def test_secret():
    secret = os.environ.get("MYSECRET")
    assert secret
    assert len(secret) == 6