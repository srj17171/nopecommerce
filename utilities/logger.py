import inspect
import logging


class LogGen:

    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler("C:\\Users\\suraj\\Desktop\\automation project\\new project nope commerce\\logs\\automation.log")
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
        logfile.setFormatter(format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger