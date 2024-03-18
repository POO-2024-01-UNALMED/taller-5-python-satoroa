from .animal import Animal

class Reptil(Animal):
    iguanas = 0
    serpientes = 0

    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        cls.iguanas += 1
        return cls(nombre, edad, "humedal", genero, "verde", 3)

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        cls.serpientes += 1
        return cls(nombre, edad, "jungla", genero, "blanco", 1)
