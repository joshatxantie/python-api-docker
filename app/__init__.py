from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)



from app.views import HelloWorld

api.add_resource(HelloWorld, '/')