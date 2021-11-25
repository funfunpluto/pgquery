import psycopg2

def pgconnect(ip, dbname):
    conn_string = f"user='hz028' password='hz028' host='{ip}' port='80' dbname='{dbname}'"
    print(conn_string)
    connection = psycopg2.connect(conn_string)
    cursor = connection.cursor()
    return cursor

def psql_exc(cursor,exc_string):
    cursor.execute(exc_string)
    result = cursor.fetchall()
    return result


def number_of_records(cursor,tblname):
    count_string = f"select count(*) from {tblname};"
    num = psql_exc(cursor,ount_string)
    return num


def distinct_colors(cursor, tblname):
    color_string =f"select distinct count(favorite_color) from {tblname};"
    color = psql_exc(cursor,color_string)
    return color

def distinct_genders(cursor, tblname):
    gendergp_string =f"select gender, count(*) from {tblname} group by gender;"
    gendergp = psql_exc(cursor,gendergp_string)
    return gendergp
