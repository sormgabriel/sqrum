from flask import request, Flask, jsonify, abort

app = Flask(__name__)
userstories = []
def current_position():
  if len(userstories)==0:
    return_value=0
  else:
    return_value= len(userstories)-1
  return return_value
@app.route('/sqrum/api/v1.0/userstories', methods=['POST'])

def create_task():
  if not request.json or not 'rol' in request.json:
    abort(4000)
  user_story = {
    'id': current_position(),
    'rol': request.json.get('rol',""),
    'description': request.json.get('description',""),
    'done':False
  }
  userstories.append(user_story)
  return jsonify({'user_story':user_story}), 201

if __name__ == '__main__':
  app.run(debug=True)
