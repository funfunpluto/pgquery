from argparse import Action, ArgumentParser
from botocore.client import ClientError
import boto3
import time

known_drivers = ['local', 's3']
class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        if driver.lower() not in known_drivers:
            parser.error("Unkown driver. Available drivers are 'local' & 's3'")
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = ArgumentParser()
    #parser.add_argument('url', help="URL of the PostgreSQL database to backup")
    parser.add_argument('ip', help="ip address of the database server")
    parser.add_argument('dbname', help="name of the database")
    parser.add_argument('tblname', help="name of the tblname")
    parser.add_argument('--driver', '-d', help="how & where to store the backup",
            nargs=2,
            action=DriverAction,
            metavar=('driver', 'destination'),
            required=True)

    return parser

def create_bucket(bucketn):
    s3 = boto3.resource('s3')
    try:
        s3.meta.client.head_bucket(Bucket=bucketn)
    except ClientError:
        bucket = s3.create_bucket(Bucket=bucketn)

def main():
    from pgquery import pgdump, storage, pg_query

    args = create_parser().parse_args()
    url = f"postgres://{args.ip}:80/{args.dbname}"
    #dump = pgdump.dump(url)
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())
    #if args.driver == 's3':
    #    client = boto3.client('s3')
    #    create_bucket(args.destination)
    #    file_name = pgdump.dump_file_name(args.url, timestamp)
    #    print(f"Backing db up to {args.destination} in S3 as {file_name}")
    #    storage.s3(client, dump.stdout, args.destination, file_name)
    #else:
    #    file_name = pgdump.dump_file_name(args.destination, timestamp)
    #    print(f"Backing db up locally as {file_name}")
    #    outfile = open(file_name, 'wb')
    #    storage.local(dump.stdout, outfile)

    cursor = pg_query.pgconnect(args.ip, args.dbname)
    #num = pg_query.number_of_records(cursor, args.tblname)
    #color = pg_query.distinct_colors(cursor, args.tblname)
    gendergp = pg_query.distinct_genders(cursor, args.tblname)
    print(f"the database table has {gendergp} of records")
