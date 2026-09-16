class Nomina:
  
  @staticmethod
  def calcular_salario_bruto (cantidad_horas, pago_hora):
    return cantidad_horas * pago_hora

  @staticmethod
  def calcular_retencion (salario_bruto):
    return  salario_bruto * 0.125

  @staticmethod
  def calcular_salario_neto (salario_bruto, retencion):
    return salario_bruto - retencion

cantidad_horas = float(input(f"¿cuantas horas trabajo?: "))
pago_hora = float(input(f"¿cual es el pago por hora?: "))

salario_bruto = Nomina.calcular_salario_bruto (cantidad_horas, pago_hora)
retencion = Nomina.calcular_retencion (salario_bruto)
salario_neto = Nomina.calcular_salario_neto (salario_bruto, retencion)

print(f"Salario bruto: {salario_bruto}")
print(f"retencion en la fuente: {retencion}")
print(f"Salario neto: {salario_neto}")