from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorCandidato import ControladorCandidatos

app=Flask(__name__)
cors = CORS(app)
micontroladorCandidato = ControladorCandidatos()


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data
@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)
@app.route("/candidatos",methods=['GET'])
def getCandidatos():
    json=micontroladorCandidato.index()
    return jsonify(json)
@app.route("/candidatos/",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json = micontroladorCandidato.create(data)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['GET'])
def getCandidato(id):
    json=micontroladorCandidato.show(id)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['PUT'])
def modificarCandidatos(id):
    data = request.get_json()
    json=micontroladorCandidato.update(id,data)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['DELETE'])
def eliminarCandidatos(id):
    json=micontroladorCandidato.delete(id)
    return jsonify(json)



if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
