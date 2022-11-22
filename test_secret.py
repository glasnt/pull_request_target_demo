import os

def test_secret():
    secret = os.environ.get("SHAREDSECRET")
    assert secret
    assert len(secret) == 6