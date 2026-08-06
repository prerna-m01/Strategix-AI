from backend.app.core.exceptions import ValidationException


def test_validation_exception():

    exception = ValidationException("Invalid")

    assert exception.message == "Invalid"