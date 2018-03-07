import logging

class MyCatalogLogger:

    LOGGER_NAME = "my_catalog"
    logger = None

    def __init__(self):
        self.logger = logging.getLogger(self.LOGGER_NAME)
        self.config_logger()

    def config_logger(self):
        self.logger.setLevel(logging.DEBUG)

        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

    def log_debug_msg(self, msg):
        self.logger.debug(msg)

    def log_info_msg(self, msg):
        self.logger.info(msg)

    def log_warning_msg(self, msg):
        self.logger.warning(msg)

    def log_error_msg(self, msg):
        self.logger.error(msg)
