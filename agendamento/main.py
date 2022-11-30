from flask import Flask, jsonify
import urllib.request

servico = Flask(__name__)

ROTA_BARBEADORES = "http://barber_barbeadores:5000/executar/"
ROTA_DISPONIBILIDADE = "http://barber_disponibilidade:5000/executar/"
ROTA_PENTEADOS = "http://barber_penteados:5000/executar/"

DESCRICAO = "Atendimento Barber"
VERSAO = "0.0.1"

@servico.route("/sobre", methods=["GET"])
def get_info():
    return jsonify(descricao=DESCRICAO, versao=VERSAO)

@servico.route("/barber/barbeadores", methods=["GET"])
def verificar_barbeadores():
    resposta = urllib.request.urlopen(ROTA_BARBEADORES)
    resposta = resposta.read()
    return resposta.decode("utf-8")

@servico.route("/barber/penteados", methods=["GET"])
def verificar_penteados():
    resposta = urllib.request.urlopen(ROTA_DISPONIBILIDADE)
    resposta = resposta.read()
    return resposta.decode("utf-8")

@servico.route("/barber/disponibilidade", methods=["GET"])
def verificar_disponibilidade():
    resposta = urllib.request.urlopen(ROTA_PENTEADOS)
    resposta = resposta.read()
    return resposta.decode("utf-8")

@servico.route("/barber/agendar/<string:id_barbeiro>/<int:id_disponibilidade>/<int:id_penteado>", methods=["POST", "GET"])
def agendar_atendimento(id_barbeiro, id_disponibilidade, id_penteado):
    resposta = urllib.request.urlopen(ROTA_DISPONIBILIDADE+ "agendar/" + str(id_barbeiro) + "/" + str(id_disponibilidade) + "/" + str(id_penteado))
    resposta = resposta.read()
    return resposta.decode("utf-8")

