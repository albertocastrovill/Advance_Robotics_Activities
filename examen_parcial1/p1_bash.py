import math
import sys

def process_data(encoder, radio, numPulsos, t):
    # Revoluciones por Segundo
    RPS = numPulsos / encoder

    # Rapidez Lineal = RPS*Circumferencia
    circ = math.pi * (2*radio)
    Rapidez_Lineal = RPS * circ

    # Distancia Recorrida = Rapidez Lineal*Tiempo
    Distancia_Recorrida = Rapidez_Lineal * t

    # Rapidez Rotacional
    Rapidez_Rotacional = RPS * 2 * math.pi

    # Desplegar resultados
    print(f"Revoluciones por Segundo: {RPS} rev/s")
    print(f"Rapidez Lineal: {Rapidez_Lineal} cm/s")
    print(f"Distancia Recorrida: {Distancia_Recorrida} cm")
    print(f"Rapidez Rotacional: {Rapidez_Rotacional} rad/s")

if __name__ == "__main__":
    
    encoder = int(sys.argv[1])
    radio = int(sys.argv[2])
    numPulsos = int(sys.argv[3])
    t = int(sys.argv[4])

    process_data(encoder, radio, numPulsos, t)
