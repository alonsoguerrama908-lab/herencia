from clases.persona.persona import Persona
from clases.alumno.alumno import Alumno
from clases.profesor.profesor import Profesor

class Exalumno(Alumno,Profesor):
  def __init__(self):
    super().__init__()
    self.titulo=""

  def leerDatosExalumno(self):
    self.titulo = input("titulo: ")

  def mostrarDatosExalumno(self):
    print(self.titulo)