import logging
import subprocess
from datetime import datetime
from settings import (
    LOGGING,
    PG_HOST,
    PG_PORT,
    PG_USER,
    DB_NAME,
    SQL_DIR
)

logger = logging.getLogger('*')


def default_command():
    """
    Returns pg_dump command with output path
    """
    filename = f'backup-{datetime.now().strftime("%m-%d-%YT%H-%M-%S")}.sql'
    path = SQL_DIR.joinpath(filename)
    return ['pg_dump', '-h' , PG_HOST , '-p', PG_PORT, '-U', PG_USER, DB_NAME, '-f', path]


def run_command(command):
    """
    Runs pg_dump command as subprocess.
    """
    
    # avoid shenanigans
    if command[0] != 'pg_dump':
        raise Exception('Warning: run_command() is meant to only run pg_dump commands!')
    try:
        subprocess.call(command)
    except subprocess.SubprocessError as e:
        logger.error('Error at %s', 'SubprocessError', exc_info=e)
