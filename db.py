import pyodbc

class BaseDatos:
    def __init__(self, servidor="localhost", database="examen2", usuario="", password=""):
        self.__servidor = servidor
        self.__database = database
        self.__usuario = usuario
        self.__password = password
        self.__conexion = None

    def conectar(self):
        try:
            if self.__usuario and self.__password:
                # Conexión con usuario y contraseña
                self.__conexion = pyodbc.connect(
                    f"DRIVER={{SQL Server}};"
                    f"SERVER={self.__servidor};"
                    f"DATABASE={self.__database};"
                    f"UID={self.__usuario};PWD={self.__password}"
                )
            else:
                # Conexión confiable (Windows Authentication)
                self.__conexion = pyodbc.connect(
                    f"DRIVER={{SQL Server}};"
                    f"SERVER={self.__servidor};"
                    f"DATABASE={self.__database};"
                    f"Trusted_Connection=yes;"
                )
        except Exception as e:
            raise ValueError(f"No se pudo conectar a la base de datos: {e}")

    def obtener_frase(self, consecutivo):
        if self.__conexion is None:
            self.conectar()
        cursor = self.__conexion.cursor()
        pk = (consecutivo % 42) + 1  # f(n) = (n mod 42) + 1

        try:
            cursor.execute("SELECT frase FROM ExamenFinal_query WHERE id = ?", pk)
            fila = cursor.fetchone()
            if fila:
                return fila[0]
            else:
                raise ValueError(f"No se encontró frase con id {pk}")
        except Exception as e:
            raise ValueError(f"Error al consultar la frase: {e}")



