import sqlite3

conn = sqlite3.connect('sqrum.db')
print "la base se abrio exitosamente"

cursor = conn.execute("SELECT id, rol, criterio_de_aceptacion from USERSTORIES")
for row in cursor:
  print "ID = ", row[0]
  print "ROL = ", row[1]
  print "CRITERIO DE ACEPTACION = ", row[2], "\n"

print "la operacion se realizo de manera exitosa"
conn.close();
