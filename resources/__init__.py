from flask_restful import Resource, reqparse
agenda = [
    {
        'agenda_id': '1',
        'nome': 'Bruno',
        'numero contato': '88182833',
        'email': 'teste@gmail.com'
    },

    {
        'agenda_id': '2',
        'nome': 'Neylanio',
        'numero contato': '88182833',
        'email': 'teste@gmail.com'
    },

    {
        'agenda_id': '3',
        'nome': 'Gabriel do Aliexpress',
        'numero contato': '88182833',
        'email': 'teste@gmail.com'
    },

    {
        'agenda_id': '4',
        'nome': 'Luan fumador de erva',
        'numero contato': '88182833',
        'email': 'teste@gmail.com'
    }
]
class Agenda(Resource):
    def get(self):
        return {'agenda': agenda}

class Contato(Resource):
    def get(self, agenda_id):
        for contato in agenda:
            if contato['agenda_id'] == agenda_id:
                return contato
        return None
    
    def post(self, agenda_id):
        pass

    def put(self, agenda_id):
        pass

    def delete(self, agenda_id):
        pass