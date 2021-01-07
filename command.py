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


def backup_filename():
    return f'backup-{datetime.now().strftime("%m-%d-%YT%H-%M-%S")}.sql'
    

def path_to_backup_dir(filename):
    return SQL_DIR.joinpath(filename) 

    
def dump_command(output_file_path):
    """
    Returns pg_dump command with output path
    """
    return ['pg_dump', '-h' , PG_HOST , '-p', PG_PORT, '-U', PG_USER, DB_NAME, '-f', output_file_path]


def run_command(command):
    """
    Runs pg_dump command as subprocess.
    You may pass your own pg_dump command.
    Note that this only allows pg_dump commands!
    """
    # avoid shenanigans
    if command[0] != 'pg_dump':
        raise Exception('Warning: run_command() is meant to only run pg_dump commands!')
    
    success = False
    try:
        subprocess.call(command)
        success = True
    except subprocess.SubprocessError as e:
        logger.error('Error at %s', 'SubprocessError', exc_info=e)
    return success
    
