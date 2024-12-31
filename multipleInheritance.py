# herdando várias classes

class Animal:
  def __init__(self, name) -> None:
    self.name = name

  def makeSound(self):
    pass

class Mammal(Animal):
  def breastfeed(self):
    return f"{self.name}, está amamentando"

class Bird(Animal):
  def fly(self):
    return f"{self.name}, está voando"

class Bat(Mammal, Bird):
  def makeSound(self):
    return "Morcegos emitem sons ultrassônicos"

bat = Bat(name="Batman")
print("O nome do morcego é", bat.name)
print(bat.breastfeed())
print(bat.fly())
print(bat.makeSound())
