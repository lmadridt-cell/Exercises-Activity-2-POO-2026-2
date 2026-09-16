class operation:
  @staticmethod
  def operation_1(addition, x):
    return addition + x
  
  @staticmethod
  def operation_2 (x, y):
    return x + y**2

  @ staticmethod
  def operation_3(addition, x, y):
    return (addition + ( x / y ))

addition = float(input("Por favor, ingrese el valor de suma: "))
x = float(input("Por favor, ingrese el valor de x: "))
y = int(input("Por favor, ingrese el valor de y: "))
while y == 0:
  y = float(input("ingrese un valor valido para y: "))
  
addition = operation.operation_1(addition, x)
x = operation.operation_2(x, y) 
addition = operation.operation_3(addition, x, y)

print(f"El valor de la suma es: {addition}")
input("presione enter para salir")