from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from sercurity import *
from user import UserRegister
from item import *
import create_tables

app = Flask(__name__)
app.secret_key = "dflkdhfldkfhdlfkhdfldhfkldhf"
api = Api(app)

jwt = JWT(app, authenticate, identity)



api.add_resource(Item, '/item<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

app.run(debug=True)