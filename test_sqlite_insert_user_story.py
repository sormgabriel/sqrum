import sqlite3

class DatabaseInsert():
  userstories = []
  def __init__(self):  
    pass 

  def rol():
    return userstories[0]['rol']

  def description():
    return userstories[0]['description']
  def openConnection():
    conn= sqlite3.connect('sqrum.db')
    print "base de datos abierta exitosamente"
    conn.execute("INSERT INTO USERSTORIES(ID, ROL, CRITERIO_DE_ACEPTACION)\
    VALUES(1,{0},{1} )".format(rol(), description()))
    conn.commit();
    print "registros guardados de manera exitosa"
    conn.close()

