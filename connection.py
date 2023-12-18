import cx_Oracle
connection = cx_Oracle.connect(user="GASELIN", password="rootG", dsn="localhost/xe")
cursor = connection.cursor()