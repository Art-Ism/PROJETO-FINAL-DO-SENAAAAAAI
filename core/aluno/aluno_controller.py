from flask import Blueprint, request, jsonify
from core.aluno.aluno_service import AlunoService
from core.aluno.aluno import Aluno
from core.autenticacao.autenticacao import autentificacao

aluno_service = AlunoService()

aluno_controller = Blueprint('aluno', __name__, url_prefix='/alunos')

@aluno_controller.route('/', methods=['GET'])
@autentificacao
def listar_alunos():
    alunos = aluno_service.listar_alunos()
    return jsonify(alunos)

@aluno_controller.route('/', methods=['POST'])
@autentificacao
def adicionar_aluno():
    dados = request.get_json()
    obj_aluno = Aluno(id=0, nome=dados["nome"],
                      idade=dados["idade"], cpf=dados["cpf"])
    aluno = aluno_service.adicionar_aluno(obj_aluno)
    return aluno, 201

@aluno_controller.route('/<int:id>', methods=['GET'])
@autentificacao
def obter_aluno(id):
    aluno = aluno_service.obter_aluno_por_id(id)
    if aluno:
        return jsonify(aluno)
    else:
        return jsonify({"erro": "Aluno não foi encontrado"}), 404
    
@aluno_controller.route('/<int:id>', methods=['DELETE'])
@autentificacao
def remover_aluno(id):
    sucesso = aluno_service.remover_aluno(id)
    return jsonify(sucesso)

@aluno_controller.route('/', methods=['PUT'])
@autentificacao
def atualizar_aluno():
    dados = request.get_json()
    obj_aluno = Aluno(id=dados["id"], nome=dados["nome"],
                      idade=dados["idade"], cpf=dados["cpf"])
    aluno = aluno_service.atualizar_aluno(obj_aluno)
    if aluno:
        return jsonify(aluno)
    else:
        return jsonify({"erro": "Aluno não encontrado"}), 404