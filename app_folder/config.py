from pathlib import Path
import logging
import sys
import mlflow


########  ------------------  MLFlow Configuration  -----------------  #########
MODEL_REGISTRY = Path("/tmp/mlflow")
Path(MODEL_REGISTRY).mkdir(parents=True, exist_ok=True)
MLFLOW_TRACKING_URI = "file://" + str(MODEL_REGISTRY.absolute())
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
print (mlflow.get_tracking_uri())


########  ------------------  Logging Configuration  -----------------  #########
LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(parents=True, exist_ok=True)

logging_config = {"version" : 1,
                  "disable_existing_loggers" : False,
                  "formatters" : {"minimal" : {"format" : "%(message)s"},
                                  "detailed" : {"format" : "%(levelname)s - %(asctime)s - [%(name)s:%(filename)s:%(funcName)s:%(lineno)d]\n%(message)s\n"}},
                  "handlers" : {"console" : {"class" : "logging.StreamHandler",
                                             "stream" : sys.stdout,
                                             "formatter" : "minimal",
                                             "level" : logging.DEBUG},
                                "info" : {"class": "logging.handlers.RotatingFileHandler",
                                         "filename": Path(LOGS_DIR, "info.log"),
                                         "maxBytes": 10485760,  # 1 MB
                                         "backupCount": 10,
                                         "formatter": "detailed",
                                         "level": logging.INFO},
                                "error" : {"class" : "logging.handlers.RotationgFileHandler",
                                           "filename" : Path(LOGS_DIR, "error.log"),
                                           "maxBytes" : 1048576,
                                           "backupCount" : 10,
                                           "formatter" : "detailed",
                                           "level" : logging.ERROR}},
                    "root" : {"handlers" : ["console", "info", "error"],
                              "level" : logging.INFO,
                              "propagate" : True}
                    }

logging.config.dictConfig(logging_config)
logger = logging.getLogger()



