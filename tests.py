import pytest
from settings import SQL_DIR
from command import (
    backup_filename,
    path_to_backup_dir,
    dump_command,
    run_command
)


@pytest.mark.freeze_time('11-19-1493T00-00-00')
def test_backup_filename_returns_string_with_datetime():
    filename = backup_filename()
    assert filename == 'backup-11-19-1493T00-00-00.sql'


@pytest.mark.freeze_time('11-19-1493T00-00-00')
def test_path_to_backup_dir_includes_correct_filename():
    # note: normally returns Path object, needs to be cast as str
    path = str(path_to_backup_dir(backup_filename()))
    sql_dir = str(SQL_DIR)
    backup_path = f'{sql_dir}/backup-11-19-1493T00-00-00.sql'
    assert path == backup_path
