class Animal:
    totalAnimales = 0
    totalMamiferos = 0
    totalAves = 0
    totalReptiles = 0
    totalPeces = 0
    totalAnfibios = 0

    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        Animal.totalAnimales += 1

    @staticmethod
    def totalPorTipo():
        return f"Mamiferos : {Animal.totalMamiferos}\nAves : {Animal.totalAves}\nReptiles : {Animal.totalReptiles}\nPeces : {Animal.totalPeces}\nAnfibios : {Animal.totalAnfibios}"

    def toString(self):
        return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"
    
    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getHabitat(self):
        return self._habitat

    def getGenero(self):
        return self._genero

    def setNombre(self, nombre):
        self._nombre = nombre

    def setEdad(self, edad):
        self._edad = edad

    def setHabitat(self, habitat):
        self._habitat = habitat

    def setGenero(self, genero):
        self._genero = genero
