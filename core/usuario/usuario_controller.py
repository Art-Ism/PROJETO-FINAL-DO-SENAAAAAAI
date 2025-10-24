from flask import Blueprint, request, jsonify
from core.usuario.usuario_service import UsuarioService
from core.usuario.usuario import Usuario

usuario_service = UsuarioService()

usuario_controller = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario_controller.route('/', methods=['GET'])
def listar_usuario():
    usuario = usuario_service.listar_usuario()
    return jsonify(usuario)

@usuario_controller.route('/', methods=['POST'])
def adicionar_usuario():
    dados = request.get_json()
    obj_usuario = Usuario(id=0, usuario=dados["usuario"],
                      senha=dados["senha"], ativo=dados["ativo"])
    usuario = usuario_service.adicionar_usuario(obj_usuario)
    return usuario(usuario), 201

@usuario_controller.route('/<int:id>', methods=['GET'])
def obter_usuario(id):
    usuario = usuario_service.obter_usuario_por_id(id)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({"erro": "Usuario não foi encontrado"}), 404
    
@usuario_controller.route('/<int:id>', methods=['DELETE'])
def remover_usuario(id):
    sucesso = usuario_service.remover_usuario(id)
    return jsonify(sucesso)

@usuario_controller.route('/', methods=['PUT'])
def atualizar_usuario():
    dados = request.get_json()
    obj_usuario = Usuario(id=dados["id"], usuario=dados["usuario"],
                       senha=dados["senha"], ativo=dados["ativo"])
    usuario = usuario_service.atualizar_usuario(obj_usuario)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({"erro": "Usuario não encontrado"}), 404