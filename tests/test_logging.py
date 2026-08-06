from backend.app.core.logger import logger


def test_logger():

    logger.info("Testing Logger")

    assert logger is not None