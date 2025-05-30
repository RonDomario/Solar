from colorama import init, Fore
import logging
import sys


init(autoreset=True)


class ColoredFormatter(logging.Formatter):
    COLORS = {
        "INFO": Fore.WHITE,
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED,
        "CRITICAL": Fore.MAGENTA
    }

    def format(self, record):
        log_color = self.COLORS.get(record.levelname, Fore.WHITE)
        log_message = super().format(record)
        return log_color + log_message


def set_logger(log_file: str):
    logger = logging.getLogger("Logger")
    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(ColoredFormatter("%(asctime)s - %(levelname)s - %(message)s"))
    console_handler.flush = lambda: console_handler.stream.flush()

    file_handler = logging.FileHandler(log_file, encoding="UTF-8")
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    file_handler.flush = lambda: file_handler.stream.flush()

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger
