from pathlib import Path
import logging
import logging.config
import environ


env = environ.Env()
environ.Env.read_env()

# aws
AWS_S3_BUCKET_NAME = env('AWS_S3_BUCKET_NAME')

# Path where the output directory is located
SQL_DIR = Path(env('SQL_DIR'))

# Path where the logfile will be created
LOG_DIR = Path(env('LOG_DIR'))

# postgreSQL settings
PG_HOST = env('PG_HOST')
PG_PORT = env('PG_PORT')
PG_USER = env('PG_USER')
DB_NAME = env('DB_NAME')

LOGGING = logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console':{
            'level': env.str('DEBUG_LEVEL', 'DEBUG'),
            'class':'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'rotating_log_file': {
            'level': env.str('DEBUG_LEVEL', 'DEBUG'),
            'class':'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename' : env('LOG_DIR'),
            'maxBytes' : env.int('MAX_BYTES', 2097152), # default 2MB (1024*1024*2)
            'backupCount' : env.int('BACKUP_COUNT', 10) # default 10 files
        }
    },
    'loggers': {
        '*': {
            'handlers': ['console', 'rotating_log_file'],
            'level': env.str('DEBUG_LEVEL', 'DEBUG')
        }
    }
})
