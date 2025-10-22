from flask import Blueprint, request, jsonify
from core.professor.professor_service import ProfessorService
from core.professor.professor import Professor

professor_service = ProfessorService()

professor_controller = Blueprint('professor', __name__, url_prefix='/professor')

@professor_controller.route('/', methods=['GET'])
def listar_professor():
    professor = professor_service.listar_professor()
    return jsonify(professor)

@professor_controller.route('/', methods=['POST'])
def adicionar_professor():
    dados = request.get_json()
    obj_professor = Professor(id=0, nome=dados["nome"],
                      formacao=dados["formacao"], idade=dados["idade"])
    professor = professor_service.adicionar_professor(obj_professor)
    return professor(professor), 201

@professor_controller.route('/<int:id>', methods=['GET'])
def obter_professor(id):
    professor = professor_service.obter_professor_por_id(id)
    if professor:
        return jsonify(professor)
    else:
        return jsonify({"erro": "professor não foi encontrado"}), 404
    
@professor_controller.route('/<int:id>', methods=['DELETE'])
def remover_professor(id):
    sucesso = professor_service.remover_professor(id)
    return jsonify(sucesso)

@professor_controller.route('/', methods=['PUT'])
def atualizar_professor():
    dados = request.get_json()
    obj_professor = Professor(id=dados["id"], nome=dados["nome"],
                       idade=dados["idade"], formacao=dados["formacao"])
    professor = professor_service.atualizar_professor(obj_professor)
    if professor:
        return jsonify(professor)
    else:
        return jsonify({"erro": "Professor não encontrado"}), 404