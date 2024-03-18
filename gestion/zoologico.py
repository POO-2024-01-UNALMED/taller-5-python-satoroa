class Zoologico:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.zonas = []

    def agregarZonas(self, zona):
        self.zonas.append(zona)

    def cantidadTotalAnimales(self):
        total = 0
        for zona in self.zonas:
            total += zona.cantidadAnimales()
        return total
