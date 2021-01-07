import logging
import subprocess
from datetime import datetime
from settings import (
    LOGGING,
    PG_HOST,
    PG_PORT,
    PG_USER,
    DB_NAME
)

logger = logging.getLogger('*')


def build_command():
    filename = f'backup-{datetime.now().strftime("%m-%d-%YT%H-%M-%S")}.sql'
    return ['pg_dump', '-h' , PG_HOST , '-p', PG_PORT, '-U', PG_USER, DB_NAME, '>', filename]


def run_command(command):
    subprocess.call(command)


def main():
    run_command(build_command())


if __name__ == '__main__':
    main()