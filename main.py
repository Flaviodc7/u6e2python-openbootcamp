class Alumno:
    nombre = "Jorge"
    nota = 7

    def cambioNombre(self):
        self.nombre = "Eduardo"

    def cambioNota(self):
        self.nota = 4

    def mostrarNombre(self):
        return self.nombre

    def mostrarNota(self):
        return self.nota

    def aprobado(self):
        if self.nota >= 7:
            return "Aprobado"
        else:
            return "Desaprobado"

p = Alumno()
p.cambioNombre()
p.cambioNota()
print(p.nombre, "está:", p.aprobado())