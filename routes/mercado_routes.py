from model.mercado_model import listar, obter, salvar, alterar, excluir, MercadoNaoEncontrado
from flask import Blueprint, jsonify, request
from config import db

mercado_blueprint = Blueprint("mercado", __name__)

@mercado_blueprint.route("/obter/<int:id>", methods= ["GET"])
def obter_mercado(id):
    try:
        mercado = obter(id)
        return jsonify(mercado), 200
    except MercadoNaoEncontrado as e:
        return jsonify({ "message": str(e)} ), 404

@mercado_blueprint.route("/listar", methods= ["GET"])
def listar_mercado():
    return jsonify(listar()), 200

@mercado_blueprint.route("/salvar", methods= ["POST"])
def salvar_mercado():
    try:
        mercado = request.json
        salvar(mercado)
        return jsonify({ "message": "Mercado cadastrado com sucesso." }), 200
    except MercadoNaoEncontrado as e:
        return jsonify({ "message": str(e) }), 404
    
@mercado_blueprint.route("/alterar", methods= ["PUT","POST"])
def alterar_mercado():
    try:
        mercado = request.json
        if (mercado["id"] > 0):
            alterar(mercado)
            return jsonify({ "message": "Mercado alterado com sucesso."}), 200
        else: 
            return jsonify({ "message": "Id do Mercado inválido." }), 404
    except MercadoNaoEncontrado as e:
        return jsonify({ "message": str(e) }), 404
    
@mercado_blueprint.route("/excluir", methods= ["DELETE","POST"])
def excluir_mercado():
    try:
        mercado = request.json
        excluir(mercado["id"])
        return jsonify({ "message": "Mercado excluído com sucesso." }), 200
    except MercadoNaoEncontrado as e:
        return jsonify({ "message": str(e) }), 404


