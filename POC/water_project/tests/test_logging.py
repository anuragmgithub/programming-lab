import logging
from logging_config import setup_logging

def test_logging_configuration():
    setup_logging()
    logger = logging.getLogger("test_logger")
    assert logger.level == logging.DEBUG

    # Test a sample log message
    logger.info("Test log message")
