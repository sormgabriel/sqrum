from flask import request, Flask, jsonify, abort
from  sqrum_db_connection import get_db

app = Flask(__name__)
@app.route('/')
def index():
    cur = get_db().cursor()
    cur.execute('select * from USERSTORIES')
    entries = [dict(id=row[0], rol=row[1], description=row[2]) for row in cur.fetchall()]
    return jsonify({'entries':entries})
       
@app.route('/sqrum/api/v1.0/userstories', methods=['POST'])

def create_task():
  if not request.json or not 'rol' in request.json:
    abort(4000)
  user_story = {
    'id': request.json.get('id',""),
    'rol': request.json.get('rol',""),
    'description': request.json.get('description',""),
  }
  cur = get_db()
  cur.cursor().execute('insert into USERSTORIES (id,rol, criterio_de_aceptacion) values (?,?,?)',[user_story['id'],user_story['rol'],user_story['description']]) 
  cur.commit()
  return jsonify({'user_story':user_story}), 201

if __name__ == '__main__':
  app.run(debug=True)
