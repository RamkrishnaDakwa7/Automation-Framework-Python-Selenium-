import logging

class  Logger:
    @staticmethod
    def CustomLogger():
        logging.basicConfig(filename="..\Logs\Automation.log",format='%(asctime)s:%(message)s',datefmt='%m%d%Y')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger