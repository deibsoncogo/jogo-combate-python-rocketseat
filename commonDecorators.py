# criando um decorador comum da classe

class MyClass:
  amount = 10

  def __init__(self, name) -> None:
    self.name = name

  def instanceMethod(self):
    return f"Método de instância, nome {self.name} e valor de {self.amount}"

  @classmethod
  def classMethod(cls):
    return f"Método de class, sem nome e valor de {cls.amount}"

  @staticmethod
  def staticMethod():
    return f"Método estático, não recebe nenhum argumento"

myObject = MyClass(name="Common")

print(myObject.instanceMethod())
print(MyClass.staticMethod())
print(MyClass.classMethod())
print("Valor da classe é", MyClass.amount)
