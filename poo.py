# criação de objeto a partir dos instancia de classes

class People:
  def __init__(self, name, age) -> None:
    self.name = name
    self.age = age

  def greeting(self):
    return f"Olá, meu nome é {self.name} e eu tenho {self.age} anos"

people1 = People("Alice", 30)

messagePeople1 = people1.greeting()
print(messagePeople1)
