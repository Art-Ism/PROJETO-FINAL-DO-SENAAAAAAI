from flask import Blueprint, request, jsonify
from core.materias.materias_service import MateriasService
from core.materias.materias import Materias

materias_service = MateriasService()

materias_controller = Blueprint('materias', __name__, url_prefix='/materias')

@materias_controller.route('/', methods=['GET'])
def listar_materias():
    materias = materias_service.listar_materias()
    return jsonify(materias)

@materias_controller.route('/', methods=['POST'])
def adicionar_materias():
    dados = request.get_json()
    obj_materias = Materias(id=0, nome=dados["nome"],
                      sigla=dados["sigla"], descricao=dados["descriacao"])
    materias = materias_service.adicionar_materias(obj_materias)
    return materias(materias), 201

@materias_controller.route('/<int:id>', methods=['GET'])
def obter_materias(id):
    materias = materias_service.obter_materias_por_id(id)
    if materias:
        return jsonify(materias)
    else:
        return jsonify({"erro": "materias não foi encontrado"}), 404
    
@materias_controller.route('/<int:id>', methods=['DELETE'])
def remover_materias(id):
    sucesso = materias_service.remover_materias(id)
    return jsonify(sucesso)

@materias_controller.route('/', methods=['PUT'])
def atualizar_materias():
    dados = request.get_json()
    obj_materias = Materias(id=dados["id"], nome=dados["nome"],
                       idade=dados["idade"], formacao=dados["formacao"])
    materias = materias_service.atualizar_materias(obj_materias)
    if materias:
        return jsonify(materias)
    else:
        return jsonify({"erro": "Materias não encontrado"}), 404