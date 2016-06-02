from flask import request, Flask, jsonify, abort

app = Flask(__name__)
tasks = []
def current_position():
  if len(tasks)==0:
    return_value=0
  else:
    return_value= len(tasks)-1
  return return_value
@app.route('/todo/api/v1.0/tasks', methods=['POST'])

def create_task():
  if not request.json or not 'title' in request.json:
    abort(4000)
  task = {
    'id': current_position(),
    'rol': request.json.get('title',""),
    'description': request.json.get('description',""),
    'done':False
  }
  tasks.append(task)
  return jsonify({'task':task}), 201

if __name__ == '__main__':
  app.run(debug=True)
