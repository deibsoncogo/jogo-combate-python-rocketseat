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

  def receiveAttack(self, damage):
    self.__life -= damage

    if self.__life < 0:
      self.__life = 0

  def attack(self, target):
    damage = self.__level * 2
    target.receiveAttack(damage)
    print(f"{self.getName()} atacou {target.getName()} e causou {damage} de dano!")

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

class Game:
  def __init__(self) -> None:
    self.hero = Hero(name="Herói", life=100, level=5, ability="Super Força")
    self.enemy = Enemy(name="Morcego", life=50, level=3, type="Voador")

  def startBattle(self):
    print("Iniciando a batalha")

    while self.hero.getLife() > 0 and self.enemy.getLife() > 0:
      print("\nDetalhes dos personagens:")

      print(self.hero.getDetails())
      print(self.enemy.getDetails())

      input("\nPressione enter para atacar")
      option = input("Escolha (1 - Ataque normal, 2 - Ataque especial): ")

      if option == "1":
        self.hero.attack(self.enemy)
      else:
        print("Escolha inválida, escolha novamente")

    if self.hero.getLife() > 0:
      print("\nParabéns, você venceu a batalha!")
    else:
      print("\nVocê foi derrotado!")

game = Game()
game.startBattle()
