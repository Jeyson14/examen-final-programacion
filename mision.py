class Mision:
    def __init__(self, frase):
        self.__frase = frase
        self.__funciones_usadas = []

    def limpiar_simbolos(self):
        self.__frase = ''.join(c for c in self.__frase if c.isalnum() or c.isspace())
        self.__funciones_usadas.append("isalnum / isspace / join")

    def normalizar_espacios(self):
        self.__frase = ' '.join(self.__frase.split())
        self.__funciones_usadas.append("split / join")

    def capitalizar(self):
        self.__frase = self.__frase.title()
        self.__funciones_usadas.append("title")

    def resolver_todas(self):
        try:
            self.limpiar_simbolos()
            self.normalizar_espacios()
            self.capitalizar()
        except Exception as e:
            raise ValueError(f"Error al resolver la frase: {e}")

    def obtener_frase(self):
        return self.__frase

    def funciones_usadas(self):
        return self.__funciones_usadas



