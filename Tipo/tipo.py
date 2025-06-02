from math import pi

def circunferencia(raio: float) -> float:
    return 2 * pi * raio

print(circunferencia.__annotations__)


print(circunferencia(8))