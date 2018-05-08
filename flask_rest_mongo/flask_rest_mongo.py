# coding:utf-8

from flask_mongoengine import MongoEngine

from flask_mongorest import MongoRest
from flask_mongorest.views import ResourceView
from flask_mongorest.resources import Resource
from flask_mongorest import methods

from flask import Flask


db = MongoEngine()


app = Flask(__name__,static_url_path='/r/s/static')
app.config.from_object('config')
db.init_app(app)
api = MongoRest(app)

#### MODELO ####
class Professor(db.Document):
    nome = db.StringField(max_length=60, required=True)

#### CARGA ####
prof = Professor(nome='Fulano1')
prof.save()
prof = Professor(nome='Fulano2')
prof.save()
prof = Professor(nome='Fulano3')
prof.save()

#### REST ####
#curl http://127.0.0.1:5000/professor/consulta/
class  ProfessoresResource(Resource):
    document = Professor
@api.register(name='professore', url='/professor/consulta/')
class ProfessoresView(ResourceView):
    resource = ProfessoresResource
    methods = [methods.Create, methods.Update, methods.Fetch, methods.List]



@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
