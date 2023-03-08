from flask_restful import Resource, reqparse
agenda = [
    {
        'agenda_id': '1',
        'nome': 'Jarbas Vasconselos',
        'numero contato': '88182833',
        'email': 'teste@gmail.com',
        'cidade' : 'juazeiro do norte'
    },

    {
        'agenda_id': '2',
        'nome': 'Firmino Mimoso',
        'numero contato': '88182833',
        'email': 'teste@gmail.com',
        'cidade' : 'juazeiro do norte'
    },

    {
        'agenda_id': '3',
        'nome': 'Gabriel do Aliexpress',
        'numero contato': '88182833',
        'email': 'teste@gmail.com',
        'cidade' : 'juazeiro do norte'
    },

    {
        'agenda_id': '4',
        'nome': 'Luan fumador de erva',
        'numero contato': '88182833',
        'email': 'teste@gmail.com',
        'cidade' : 'juazeiro do norte'
    }
]


class AgendaModel:
    def __init__(self, agenda_id, nome, numero, email, cidade) -> None:
        self.agenda_id = agenda_id
        self.nome = nome
        self.numero = numero
        self.email = email
        self.cidade = cidade

class Agenda(Resource):
    def get(self):
        return {'agenda': agenda}

class Contato(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('numero contato')
    argumentos.add_argument('email')
    argumentos.add_argument('cidade')


    def find_agenda(agenda_id):
        for contato in agenda:
            if contato['agenda_id'] == agenda_id:
                return contato
        return None

    def get(self, agenda_id):
        contato = Contato.find_agenda(agenda_id)
        if contato:
            return contato
        return {'message': 'contato not found'}, 404

    def post(self, agenda_id):
        dados = Contato.argumentos.parse_args()
        novo_contato = {'agenda_id': agenda_id, **dados}
        agenda.append(novo_contato)
        return novo_contato, 200

    def put(self, agenda_id):
        dados = Contato.argumentos.parse_args()
        novo_contato = {'agenda_id': agenda_id, **dados}
        pointer_contato = Contato.find_agenda(agenda_id)
        if pointer_contato:
            pointer_contato.update(novo_contato)
            return novo_contato, 200
        agenda.append(novo_contato)
        return novo_contato, 201

    def delete(self, agenda_id):
        global agenda
        agenda = [contato for contato in agenda if contato['agenda_id'] != agenda_id]
        return {'message': 'Contato deleted.'}