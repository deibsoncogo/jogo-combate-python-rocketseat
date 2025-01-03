class Character:
  def __init__(self, name, life, level):
    self.__name = name
    self.__life = life
    self.__level = level

  def getName(self):
    return self.__name

  def getLife(self):
    return self.__life

  def getLevel(self):
    return self.__level

  def getDetails(self):
    return f"\nNome: {self.getName()}\nVida: {self.getLife()}\nNível: {self.getLevel()}"

class Hero(Character):
  def __init__(self, name, life, level, ability):
    super().__init__(name, life, level)
    self.__ability = ability

  def getAbility(self):
    return self.__ability

  def getDetails(self):
    return f"{super().getDetails()}\nHabilidade: {self.getAbility()}"

class Enemy(Character):
  def __init__(self, name, life, level, type):
    super().__init__(name, life, level)
    self.__type = type

  def getType(self):
    return self.__type

  def getDetails(self):
    return f"{super().getDetails()}\nTipo: {self.getType()}"

hero = Hero(name="Herói", life=100, level=5, ability="Super Força")
print(hero.getDetails())

enemy = Enemy(name="Morcego", life=50, level=3, type="Voador")
print(enemy.getDetails())
