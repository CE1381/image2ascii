from image2ascii.logger import get_default_logger

logger = get_default_logger()


def get_say_hello(name: str) -> str:
    logger.info("SAY-HELLO-WORKED")
    return f"Hello, {name}"
