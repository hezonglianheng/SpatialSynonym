# encoding: utf8
import logging


def get_logger(logfile: str):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        s_handler = logging.StreamHandler()
        s_formatter = logging.Formatter(
            '{asctime}:{levelname}:{message}',
            style='{'
        )
        s_handler.setFormatter(s_formatter)
        logger.addHandler(s_handler)

        f_handler = logging.FileHandler(logfile,
                                        encoding='utf8')
        f_formatter = logging.Formatter(
            '{asctime}:{levelname}:{message}',
            style='{'
        )
        f_handler.setFormatter(f_formatter)
        logger.addHandler(f_handler)


if __name__ == '__main__':
    get_logger('log.txt')
    logging.info('this is a log.')
