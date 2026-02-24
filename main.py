from clases.exalumno.exalumno import Exalumno

def main():
    exalumno = Exalumno()
    exalumno.leerDatosPersona()
    exalumno.leerDatosAlumno()
    exalumno.leerDatosProfesor()
    exalumno.leerDatosExalumno()

    exalumno.mostrarDatosPersona()  
    exalumno.mostrarDatosAlumno()
    exalumno.mostrarDatosProfesor()
    exalumno.mostrarDatosExalumno()
if __name__ == "__main__" :
    main()

