from flask import Flask, request
# from resources.models import class_api
from resources.user import User,Content, Post
from flask_mongoengine import MongoEngine
from flask_cors import CORS

app = Flask(__name__, static_folder='E:/sei1213/unit4/CAPSTONE/CAPSTONE/frontend', static_url_path='')
# app.register_blueprint(class_api, url_prefix='/api/v1')
app.config['MONGODB_SETTINGS']= {
    'db': 'FIRESIDE',
    'host':'127.0.0.1',
    'port':27017
}
db = MongoEngine(app)
app.config['MONGODB_CONNECT'] = False
@app.route('/posttest', methods=['POST', 'GET', 'DELETE', 'PUT'])
def methodtest():
    return f'this the method {request.method}'
@app.route('/')
def homePage():
    return {"Hello":["world","my name is", "Michael"]}
@app.route('/user/signup')

@app.route('/classes')
def classPage():
    return {"Class":["This is the classes page"]}


@app.route('/classes/create')
def createClass():
    return '<h1>Create a Class Here</h1>'


@app.route('/monsters')
def monsterPage():
    return {"Monster": ["this is the monster page"]}


@app.route('/monsters/create', methods=['POST', 'GET'])
def createMonster():
    print(request.get_json())
    return "<h1>Create a Monster Here</h1>"


# @app.route('/items')
# def itemList():
#     return {"Item List Page":["Item 1","Item 2", "Item 3"]}
# @app.route('/spells')
# def spellTable():
#     return {"Spells":["spell 1 ", "spell 2"]}
# @app.route('/abilities')
# def abilityTable():
#     return {"Abilites":["Abilites will go here"]}


if __name__ == "__main__":
    app.run(debug=True)
