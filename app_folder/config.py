from pathlib import Path
import logging
import sys

LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(parents=True, exist_ok=True)

logging_config = {"version" : 1,
                  "disable_existing_loggers" : False,
                  "formatters" : {"minimal" : {"format" : "%(message)s"},
                                  "detailed" : {"format" : "%(levelname)s - %(asctime)s - [%(name)s:%(filename)s:%(funcName)s:%(lineno)d]\n%(message)s\n"}},
                  "handlers" : {"console" : {"class" : "logging.StreamHandler",
                                             "filename" : Path(LOGS_DIR, "info.log"),
                                             "maxBytes": 10485760,  # 1 MB
                                             "backupCount" : 10,
                                             "formatter" : "detailed",
                                             "level" : logging.INFO},
                                "info": {"class": "logging.handlers.RotatingFileHandler",
                                         "filename": Path(LOGS_DIR, "info.log"),
                                         "maxBytes": 10485760,  # 1 MB
                                         "backupCount": 10,
                                         "formatter": "detailed",
                                         "level": logging.INFO},
                                }}



