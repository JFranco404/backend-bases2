import cx_Oracle
connection = cx_Oracle.connect(user="BATMAN", password="batroot", dsn="localhost/xe")
cursor = connection.cursor()