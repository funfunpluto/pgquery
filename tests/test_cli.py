#pgquery pastgres://bob@example.com:5432/db_one --driver s3 backups

import pytest
from pgquery import cli

#url = "postgres://bob@example.com:5432/db_one --driver s3 backups"
ip = "127.0.0.1"
dbname = "postgres_db"
tblname = "postgres_db_tbl"

@pytest.fixture 
def parser():
    return cli.create_parser()

def test_parser_without_driver(parser):
    """
    without a specified driver the parser will exit

    """
    with pytest.raises(SystemExit):
        parser.parse_args([ip, dbname, tblname])

def test_parser_with_unknown_driver(parser):
    """
    the parser will exit if it the driver name is unknown

    """
    with pytest.raises(SystemExit):
        parser.parse_args([ip, dbname, tblname, '--driver', 'azure', 'destination'])

def test_parser_with_known_driver(parser):
    """
    the parser will not exit if it the driver name is known

    """
    for driver in ['local','s3']:
        assert parser.parse_args([ip, dbname, tblname, '--driver', driver, 'destination'])


def test_parser_with_driver(parser):
    """
    the parser will exit if it receives a driver without a destination

    """
    with pytest.raises(SystemExit):
        parser.parse_args([ip,dbname, tblname, "--driver", "local"])


def test_parser_with_driver_and_destination(parser):
    """
    the parser will not exit if it receives a driver and a destination

    """
    args = parser.parse_args([ip, dbname,tblname, '--driver', 'local', '/home/path'])

    assert args.ip == ip
    assert args.dbname == dbname
    assert args.tblname == tblname
    assert args.driver == 'local'
    assert args.destination == '/home/path'
