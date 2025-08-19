import json
import re

class LectorJSON:
    def __init__(self, archivo):
        self.__archivo = archivo
        self.__estudiantes = []

    def leer(self):
        with open(self.__archivo, "r", encoding="utf-8") as f:
            self.__estudiantes = json.load(f)  # JSON es una lista directamente

    def limpiar(self, texto):
        texto = texto.upper()
        texto = re.sub(r'[^A-ZÑÁÉÍÓÚ ]', '', texto)
        texto = re.sub(r'\s+', ' ', texto).strip()
        return texto

    def filtrar(self, nombre_completo):
        nombre_completo = self.limpiar(nombre_completo)
        for est in self.__estudiantes:
            est_nombre = self.limpiar(est.get("nombre", "")) + " " + self.limpiar(est.get("apellido", ""))
            if nombre_completo == est_nombre:
                return est
        raise ValueError("Estudiante no encontrado en JSON")



