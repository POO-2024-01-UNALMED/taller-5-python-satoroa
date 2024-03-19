import zooAnimales

class Animal:
    _totalAnimales = 0
    totalMamiferos = 0
    totalAves = 0
    totalReptiles = 0
    totalPeces = 0
    totalAnfibios = 0
    _zona = ""

    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        Animal.totalAnimales += 1

    def movimiento():
        return "desplazarse"
    
    @staticmethod
    def totalPorTipo():
        return f"Mamiferos : {Animal.totalMamiferos}\nAves : {Animal.totalAves}\nReptiles : {Animal.totalReptiles}\nPeces : {Animal.totalPeces}\nAnfibios : {Animal.totalAnfibios}"

    def toString(self):
        if self._zona != "":
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + str(self._edad) + ", habito en " + self._habitat + " y mi genero es " + self._genero + ", la zona en la que me ubico es " + self._zona.getNombre() + ", en el zoo " + self._zona.getZoo().getNombre()
        else:
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + str(self._edad) + ", habito en " + self._habitat + " y mi genero es " + self._genero
    
    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales

    @classmethod
    def setTotalAnimales(cls, totalAnimales):
        cls._totalAnimales = totalAnimales

    @classmethod
    def getZona(cls):
        return cls._zona
    
    @classmethod
    def setZona(cls, zona):
        cls._zona = zona

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad
    
    def setEdad(self, edad):
        self._edad = edad
    
    def getHabitat(self):
        return self._habitat
    
    def setEdad(self, habitat):
        self._habitat = habitat
    
    def getGenero(self):
        return self._genero
    
    def setGenero(self, genero):
        self._genero = genero
