class Jugador:
    def __init__(self, nombre, edad, posición, club, país, número, goles, partidos, asistencias, amarillas, rojas, premios):
        self.nombre = nombre
        self.edad = edad
        self.posición = posición
        self.club = club
        self.país = país
        self.número = número
        self.goles = goles
        self.partidos = partidos
        self.asistencias = asistencias
        self.amarillas = amarillas
        self.rojas = rojas
        self.premios = premios

    def Prom_Goles(self):
        self.promedio = self.goles / self.partidos
        print(f"El promedio de goles de {self.nombre} es {self.promedio}")

    def Es_Goleador(self):
        if self.promedio >= 1:
            print(self.nombre,"Es un goleador nato")
        else:
            print(self.nombre,"No ve la pelota ni cuadrada")

    def Actualizar_Info(self):
        self.partidos = self.partidos + 1
        self.goles = self.goles + int(input(f"Cuantos Goles hizo {self.nombre} en el partido: "))
        self.asistencias = self.asistencias + int(input(f"Cuantas asistencias hizo {self.nombre} en el partido: "))
        self.amarillas = self.amarillas + int(input(f"Cuantas tarjetas amarillas recibio {self.nombre} en el partido: "))
        self.rojas = self.rojas + int(input(f"Cuantas tarjetas rojas recibio {self.nombre} en el partido: "))
    
    def Agegar_Premio(self):
        self.premios = self.premios + 1
        premio = input(f"que premio gano {self.nombre}? ")
        print(f"{self.nombre} ha ganado el premio {premio}")

    def Eliminar_Premio(self):
        self.premios = self.premios - 1
        premio = input(f"que premio le sacaron a {self.nombre}? ")
        print(f"{self.nombre} ha perdido el premio {premio}")


futbolista1 = Jugador("Joaquin", 17, "ST", "San Lorenzo", "Argentina", 33, 276, 520, 23, 45, 0, 1)

print(futbolista1.goles)
futbolista1.Actualizar_Info()
print(futbolista1.goles)
futbolista1.Prom_Goles()
futbolista1.Es_Goleador()
futbolista1.Agegar_Premio()
print(f"{futbolista1.nombre} tiene un total de: {futbolista1.premios} premios ")
futbolista1.Eliminar_Premio()
print(f"{futbolista1.nombre} tiene un total de: {futbolista1.premios} premios ")