import psycopg2

connection = None
try:
    # In PostgreSQL, default username is 'postgres' and password is 'postgres'.
    # And also there is a default database exist named as 'postgres'.
    # Default host is 'localhost' or '127.0.0.1'
    # And default port is '54322'.
    connection = psycopg2.connect("user='postgres' host='localhost' password='1234' port='5432'")
    print('Database connected.')

except:
    print('Database not connected.')

if connection is not None:
    connection.autocommit = True

    cur = connection.cursor()

    cur.execute("SELECT datname FROM pg_database;")

    list_database = cur.fetchall()

    database_name = input('Enter database name to check exist or not: ')

    if (database_name,) in list_database:
        print("'{}' Database already exist".format(database_name))
    else:
        print("'{}' Database not exist.".format(database_name))
    connection.close()
    print('Done')