class Animal:
    totalAnimales = 0
    totalMamiferos = 0
    totalAves = 0
    totalReptiles = 0
    totalPeces = 0
    totalAnfibios = 0

    def __init__(self, nombre, edad, habitat, genero):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        Animal.totalAnimales += 1

    @staticmethod
    def totalPorTipo():
        return f"Mamiferos : {Animal.totalMamiferos}\nAves : {Animal.totalAves}\nReptiles : {Animal.totalReptiles}\nPeces : {Animal.totalPeces}\nAnfibios : {Animal.totalAnfibios}"

    def toString(self):
        return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi genero es {self.genero}"
