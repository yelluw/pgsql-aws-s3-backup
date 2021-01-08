import logging
from command import dump_command, run_command, backup_filename, path_to_backup_dir
from s3 import upload_to_bucket
from settings import LOGGING


logger = logging.getLogger('*')


def backup_db():
    FILENAME = backup_filename()
    FILE_PATH = path_to_backup_dir(FILENAME)
    pg_dump_command = dump_command(FILE_PATH)
    
    success = run_command(pg_dump_command)
    if not success:
        logger.error('Creating the backup from pg_dump failed.')
        return success
    logger.info('pg_dump ran successfully')
    
    success = upload_to_bucket(str(FILE_PATH), FILENAME)
    if not success:
        logger.error('Uploading the file to AWS S3 failed.')
    logger.info('Backup file uploaded successfully to aws s3')
    return success
