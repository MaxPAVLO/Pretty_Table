import psycopg2
from prettytable import PrettyTable, from_db_cursor

conn = None
cur = None

try:
	conn = psycopg2.connect(
		host = "localhost",
		dbname = "demo",
		user = "postgres",
		password = 256809,
		port = 5433)

	cur = conn.cursor()

	cur.execute("SELECT * FROM eml")
	my_table = from_db_cursor(cur)
	print(my_table)

	conn.commit()

except Exception as error:
	print("ERROR")

finally:
	if cur is not None:
		cur.close()

	if conn is not None:
		conn.close()