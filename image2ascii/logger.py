import logging
import functools
from logging import handlers
import time
import cProfile
import pstats
from pstats import SortKey


def get_default_logger(level: str = "INFO"):
    # creating a log file
    filename = './logs/info.log'

    # config a logger formatter
    logging_msg_format = '[%(levelname)s] [%(asctime)s] :[%(filename)s],[%(funcName)s],[%(lineno)d] => %(message)s'
    logging_date_format = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(logging_msg_format, datefmt=logging_date_format)

    # config a logger handlers
    handler_file = handlers.TimedRotatingFileHandler(filename, 'midnight', 1)
    handler_file.suffix = "%Y-%m-%d"  # or anything else that strftime will allow
    handler_file.setFormatter(formatter)

    handler_stream = logging.StreamHandler()
    handler_stream.setFormatter(formatter)

    # config a logger
    logging.basicConfig(
        level=level,
        format=logging_msg_format,
        datefmt=logging_date_format,
        handlers=[handler_stream, handler_file]
    )

    logger = logging.getLogger('logger')

    return logger


def log(func):
    """decorator to wrap a functions in order to log any exception if it happened"""
    logger = get_default_logger('DEBUG')

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        logger.debug(f"function {func.__name__} called with args {signature}")
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logger.exception(f"Exception raised in {func.__name__}. exception: {str(e)}")

    return wrapper


def timer(func):
    """print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        prof = cProfile.Profile()
        prof.enable()
        value = func(*args, **kwargs)
        prof.disable()
        profile_time = time.time()
        prof.dump_stats(f'profile/{func.__name__!r}_{profile_time}.prof')
        p = pstats.Stats(f'profile/{func.__name__!r}_{profile_time}.prof')
        p.sort_stats(SortKey.CUMULATIVE).print_stats(100)
        return value

    return wrapper_timer
