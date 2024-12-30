print("Exemplo de herança, usamos para herdar os métodos de outra classe")

class Animal:
  def __init__(self, name) -> None:
    self.name = name

  def toWalk(self):
    return print(f"O animal {self.name} andou")

  def makeSound(self):
    pass

class Dog(Animal):
  def makeSound(self):
    return "Au, au"

class Cat(Animal):
  def makeSound(self):
    return "Miau"

dog = Dog(name="Rex")
cat = Cat(name="Felix")

print(dog, cat)

print("\nExemplo de polimorfismo, reaproveitamento do código")
animals = [dog, cat]

for animal in animals:
  print(f"{animal.name} faz: {animal.makeSound()}")

print("\nExemplo de encapsulamento, forma de proteger dados")
class BankAccount:
  def __init__(self, balance):
    self.__balance = balance
    print(f"Conta criada, saldo: {self.__balance}")

  def deposit(self, amount):
    if amount > 0:
      self.__balance += amount
      print(f"Deposito realizado, saldo: {self.getBalance()}")
    else:
      print("Deposito inválido, valor negativo")

  def withdraw(self, amount):
      if amount > 0 and amount <= self.__balance:
        self.__balance -= amount
        print(f"Saque realizado, saldo: {self.getBalance()}")
      else:
        print("Saque inválido, valor negativo ou sem saldo")

  def getBalance(self):
      return self.__balance

account = BankAccount(balance=1000)
account.deposit(amount=500)
account.withdraw(amount=20)
account.deposit(amount=-10)

print("\nExemplo de abstração, método para definir um padrão das classes")
from abc import ABC, abstractmethod

class Vehicle(ABC):
  @abstractmethod
  def on(self):
    pass

  @abstractmethod
  def off(self):
    pass

class Car(Vehicle):
  def __init__(self) -> None:
    pass

  def on(self):
    return "Carro ligado"

  def off(self):
    return "Carro desligado"

carBlue = Car()

print(carBlue.on())
print(carBlue.off())
