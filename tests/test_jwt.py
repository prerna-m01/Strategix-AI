from backend.app.auth.jwt import (
    create_access_token,
    verify_token,
)


def test_create_token():
    token = create_access_token(
        {
            "sub": "admin@strategix.ai"
        }
    )

    assert token is not None


def test_verify_token():
    token = create_access_token(
        {
            "sub": "admin@strategix.ai"
        }
    )

    payload = verify_token(token)

    assert payload["sub"] == "admin@strategix.ai"


def test_invalid_token():
    assert verify_token("invalid_token") is None