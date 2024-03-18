from .animal import Animal

class Ave(Animal):
    aguilas = 0
    halcones = 0

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        cls.halcones += 1
        return cls(nombre, edad, "montanas", genero, "cafe glorioso")

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        cls.aguilas += 1
        return cls(nombre, edad, "montanas", genero, "blanco y amarillo")
