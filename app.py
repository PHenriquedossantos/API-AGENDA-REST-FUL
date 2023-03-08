from flask import Flask
from flask_restful import Api
from resources.agenda import Agenda, Contato

app = Flask(__name__)
api = Api(app)



api.add_resource(Agenda, '/agenda')
api.add_resource(Contato, '/agenda/contato/<string:agenda_id>')


if __name__ == '__main__':
    app.run(debug=True)

