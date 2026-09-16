class calcular_edades:
  
  @staticmethod
  def calcular_edalber(edjuan):
    return (2 * edjuan) / 3

  @staticmethod
  def calcular_edana(edjuan):
    return(4 * edjuan) / 3

  @staticmethod
  def calcular_edmama(edjuan, edalber, edana):
    return edjuan + edalber + edana

edjuan = float(input("Edad de Juan: "))

edalber = calcular_edades.calcular_edalber(edjuan)
edana = calcular_edades.calcular_edana(edjuan)
edmama = calcular_edades.calcular_edmama(edjuan, edalber, edana)

print(f"Las edades son: Alberto = {edalber}, Juan = {edjuan}, Ana = {edana}, Mamá = {edmama}") 

input("Presiona Enter para cerrar...")