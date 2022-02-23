import psycopg2
import sys


con = None


conn = psycopg2.connect(
  dbname="anunciosdb",
  user="atokar",
  password="1234"
)
#     cur = con.cursor()
#     cur.execute('SELECT 1 from mytable')          
#     ver = cur.fetchone()
#     print(ver)
#
#
# except psycopg2.DatabaseError:
#     print(psycopg2.DatabaseError)   
#     sys.exit(1)
#
#
# finally:
#
#     if con:
#         con.close()