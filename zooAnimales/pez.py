from .animal import Animal

class Pez(Animal):
    salmones = 0
    bacalaos = 0

    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        cls.salmones += 1
        return cls(nombre, edad, "oceano", genero, "rojo", 6)

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        cls.bacalaos += 1
        return cls(nombre, edad, "oceano", genero, "gris", 6)
