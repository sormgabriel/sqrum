import sqlite3

conn = sqlite3.connect('sqrum.db')
print "Base de datos abierta exitosamente"

conn.execute('''CREATE TABLE USERSTORIES 
  (ID INT PRIMARY KEY NOT NULL,
   ROL TEXT NOT NULL,
   CRITERIO_DE_ACEPTACION TEXT NOT NULL);''')
print "La tabla se creo existosamente"
