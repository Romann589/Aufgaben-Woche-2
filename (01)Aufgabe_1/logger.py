import logging
from pathlib import Path


def log_error(message: str) -> None:
    logfile_path = Path(__file__).parent / "customer_app_error.log"
    logging.basicConfig(filename=logfile_path, level=logging.ERROR, force=True)
    logging.error(message)


def log_debug(message: str) -> None:
    logfile_path = Path(__file__).parent / "customer_app_debug.log"
    logging.basicConfig(filename=logfile_path, level=logging.DEBUG, force=True)
    logging.debug(message)