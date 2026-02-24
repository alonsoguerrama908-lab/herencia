from clases.persona.persona import Persona
class Profesor(Persona):
  def __init__(self):
    super().__init__()
    self.clave=""
  
  def leerDatosProfesor(self):
    self.clave = input("Clave:")

  def mostrarDatosProfesor(self):
    print(self.clave)