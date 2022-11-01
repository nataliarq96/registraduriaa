from Modelos.Candidato import Candidato
class ControladorCandidatos():
    def __init__(self):
        print("Creando Controlador Candidato")

    def index(self):
        print("Listar todas las candidato")
        unCandidato = {
            "_id": "1",
            "cédula": "123456",
            "números_resolución": "13",
            "apellido": "Ruiz",
            "nombre": "Fernando"

        }
        return unCandidato

    def create(self,elCandidato, infoCandidato):
        print("Crear un candidato")
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

    def show(self,id):
        print("Mostrando un candidato con id ", id)
        unCandidato= {
            "_id": id,
            "cédula": "123456",
            "números_resolución": "13",
            "apellido": "Ruiz",
            "nombre": "Fernando"
        }
        return unCandidato

    def update(self, id, elCandidato, infoCandidato):
        print("Actualizando candidato con id ", id)
        elCandidato=Candidato(infoCandidato)
        return elCandidato.__dict__

    def delete(self, id):
        print("Elimiando candidatocon id ", id)
        return {"deleted_count": 1}