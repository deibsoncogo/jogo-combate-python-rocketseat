# criando um decorador onde permite executar funções ou classes com facilidade

# função
def myDecoratorFunction(func):
  def wrapper():
    print("\nAntes da função ser chamada")
    func()
    print("Depois da função ser chamada")

  return wrapper

@myDecoratorFunction
def myFunction1():
  print("Primeira função chamada, decorador função")

myFunction1()

# classe
class MyDecoratorClass:
  def __init__(self, func) -> None:
    self.func = func

  def __call__(self) -> None:
    print("\nAntes da função ser chamada")
    self.func()
    print("Depois da função ser chamada")

@MyDecoratorClass
def myFunction2():
  print("Segunda função chamada, decorador classe")

myFunction2()
