import sqlite3

conn= sqlite3.connect('sqrum.db')
print "base de datos abierta exitosamente"

conn.execute("INSERT INTO USERSTORIES(ID, ROL, CRITERIO_DE_ACEPTACION)\
  VALUES(1, 'scrum_master','quiero crear una user story' )")
conn.commit();
print "registros guardados de manera exitosa"
conn.close()

