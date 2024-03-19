class Zoologico():
    _zonas = []
    def __init__(self, nombre, direccion):
        self._nombre = nombre
        self._direccion = direccion

    def agregarZonas(self, zona):
        self._zonas.append(zona)

    def cantidadTotalAnimales(self):
        total = 0
        for zona in self._zonas:
            total += zona.cantidadAnimales()
        return total

    def getNombre(self):
        return self._nombre

    def getDireccion(self):
        return self._direccion

    def getZonas(self):
        return self._zonas

    def setNombre(self, nombre):
        self._nombre = nombre

    def setDireccion(self, direccion):
        self._direccion = direccion

    @classmethod
    def getZona(cls):
        return cls._zonas
    
    @classmethod
    def setZona(cls, zonas):
        cls._zonas = zonas