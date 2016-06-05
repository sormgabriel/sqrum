import sqlite3
from flask import g
from flask import Flask, current_app

app = Flask(__name__)
DATABASE = 'sqrum.db'

def get_db():
  db = getattr(g,'__database', None) 
  if db is None:
    db = g._database = sqlite3.connect(DATABASE)
  return db
    
@app.teardown_appcontext
def close_connection(exception):
  db = getattr(g,'__database', None)
  if db is not None:
    db.close()
