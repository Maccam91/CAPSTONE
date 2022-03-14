import os
from flask import Flask, request, render_template

from flask_mongoengine import MongoEngine
from flask_mongoengine.wtf import model_form
from wtforms import validators
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()
URI = os.getenv("MONGO_URI")

app = Flask(__name__, static_folder='E:/sei1213/unit4/CAPSTONE/CAPSTONE/frontend', static_url_path='')

app.config['MONGODB_SETTINGS']= {URI or "mongodb://127.0.0.1:27017/FIRESIDE"} 
# db = MongoEngine(app)
# db.init_app(app)
app.config['MONGODB_CONNECT'] = False


# Routes
from user import routes
# @app.route('/posttest', methods=['POST', 'GET', 'DELETE', 'PUT'])
# def test():
#     return render_template('home.html')

@app.route('/')
def homePage():
    return {"Hello":["world","my name is", "Michael"]}



# @app.route('/classes')
# def classPage():
#     return {"Class":["This is the classes page"]}


# @app.route('/classes/create')
# def createClass():
#     return '<h1>Create a Class Here</h1>'


# @app.route('/monsters')
# def monsterPage():
#     return {"Monster": ["this is the monster page"]}


# @app.route('/monsters/create', methods=['POST', 'GET'])
# def createMonster():
#     print(request.get_json())
#     return "<h1>Create a Monster Here</h1>"


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
