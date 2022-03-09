from flask import jsonify, Blueprint
from flask_restful import Resource, Api
from flask_mongoengine.wtf import model_form

class ClassList(Resource):
    def get(self):
        return jsonify({'class': [{'class-name': 'SMORC'}]})
    
class Class(Resource):
    def get(self, id):
        return jsonify({'class': 'SMORC'})

class_api = Blueprint('class', __name__)
api = Api(class_api)
api.add_resource(
    ClassList,
    '/classes',
    endpoint='classes'
    
)
api.add_resource(
    Class,
    '/class/<int:id>',
    endpoint='class'

)