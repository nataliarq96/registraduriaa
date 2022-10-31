from Modelos.Mesa import Mesa
class ControladorMesa():
    def __init__(self):
        print("Creando Controlador Mesa")

    def index(self):
        print("Listar todas las mesas")
        unMesa = {
            "numero": "1",
            "números_inscritos": "13"

        }
        return [unMesa]

    def create(self,elMesa):
        print("Crear un mesa")
        elMesa = Mesa(infoMesa)
        return elMesa.__dict__

    def show(self,id):
        print("Mostrando un mesa con id ", id)
        unMesa = {
            "numero": "1",
            "números_inscritos": "13"
        }
        return [unMesa]

    def update(self, id, elMesa):
        print("Actualizando mesa con id ", id)
        elMesa = Mesa(infoMesa)
        return elMesa.__dict__

    def delete(self, id):
        print("Elimiando mesa con id ", id)
        return {"deleted_count": 1}