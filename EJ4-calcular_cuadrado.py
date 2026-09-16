class calcular_cuadrado:
  
  @staticmethod
  def cuadrado (x):
    return pow(x,2)

  @staticmethod
  def cubo (x):
    return pow(x,3)

x = float(input(f"Ingrese el numero: "))

cuadrado = calcular_cuadrado.cuadrado(x)
cubo = calcular_cuadrado.cubo(x)

print(f"El cuadrado de {x} es {cuadrado}")
print(f"El cubo de {x} es {cubo}")

input(f"Preciona enter para cerrar")