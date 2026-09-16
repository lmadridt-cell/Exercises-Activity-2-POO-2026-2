  class circulo:
  
  @staticmethod
  def area_circulo (r):
    return math.pi * pow(r,2)

  @staticmethod
  def long_circunferencia (r):
    return 2 * math.pi * r 

import math

r = float(input(f"Ingrese el valor del radio: "))

area_circulo = circulo.area_circulo (r)
long_circunferencia = circulo.long_circunferencia (r)

print(f"El area del circulo es {round(area_circulo,3)}")
print(f"longitud de la circunferencia {round(long_circunferencia,3)}")

input(f"Preciona enter para cerrar")