from backend.app.auth.hashing import (
    hash_password,
    verify_password,
)


def test_password_hashing():
    password = "Strategix123"

    hashed = hash_password(password)

    assert hashed != password

    assert verify_password(
        password,
        hashed,
    )


def test_wrong_password():
    password = "Strategix123"

    hashed = hash_password(password)

    assert not verify_password(
        "WrongPassword",
        hashed,
    )