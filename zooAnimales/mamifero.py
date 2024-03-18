from .animal import Animal

class Mamifero(Animal):
    caballos = 0
    leones = 0

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        cls.caballos += 1
        return cls(nombre, edad, "pradera", genero, True, 4)

    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        cls.leones += 1
        return cls(nombre, edad, "selva", genero, True, 4)
