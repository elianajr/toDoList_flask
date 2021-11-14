"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from sqlalchemy import exc
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_task():
    tasks = User.get_all()
    all_tasks = [task.to_dict() for task in tasks]
    return jsonify(all_tasks), 200


@app.route('/user', methods=['POST'])
def create_task():
    new_task = request.json.get('task', None)

    if not new_task:
        return jsonify({'error': 'Missing parameters'}), 400

    task = User(task=new_task)
    try:
        task_created = task.create()
        return jsonify(task_created.to.dict()), 201

    except exc.IntegrityError:
        return jsonify({'error': 'Fail in data'}), 400

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_task(id):
   task_deleted = User.delete(id)
    # if task_deleted:
    #     # return jsonify(task.to_dict()), 200
    #     return jsonify({'error': 'Task not found'}), 400



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
