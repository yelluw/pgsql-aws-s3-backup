import logging
import logging.config
import environ


env = environ.Env(
    DEBUG=(bool, False)
)

environ.Env.read_env()

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
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'rotating_log_file': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename' : 'script.log',
            'maxBytes' : 1024*1024*2, # 2MB
            'backupCount' : 10,
        }
    },
    'loggers': {
        '*': {
            'handlers': ['console'], #, 'rotating_log_file'],
            'level': 'DEBUG'
        }
    }
})
