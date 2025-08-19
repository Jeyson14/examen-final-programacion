from lector import LectorJSON
from db import BaseDatos
from mision import Mision

def main():
    # Cargar estudiantes
    lector = LectorJSON("estudiantes.json")
    lector.leer()

    nombre_completo = input("Ingrese el nombre y apellido del estudiante: ")
    try:
        estudiante = lector.filtrar(nombre_completo)
        print("✅ Encontrado:", estudiante)
    except ValueError as e:
        print("⚠ Error:", e)
        return

    # Obtener consecutivo y calcular PK
    consecutivo = estudiante["consecutivo"]
    bd = BaseDatos()
    try:
        frase = bd.obtener_frase(consecutivo)
        print("\nFrase obtenida de la base de datos:", frase)
    except ValueError as e:
        print("⚠ Error al consultar la base de datos:", e)
        return

    # Resolver misión con la clase Mision
    mision = Mision(frase)
    try:
        mision.resolver_todas()
        print("\nFrase corregida:", mision.obtener_frase())
        print("Funciones de texto usadas:", mision.funciones_usadas())
    except ValueError as e:
        print("⚠ Error al procesar la misión:", e)

if __name__ == "__main__":
    main()




