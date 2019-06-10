class Dog:
    """ a simple dog class """
    def __init__(self,name):
      self.__name= name;
    def speak(self):
        return "Woof!"
class Cat:
    """ a simple dog class """
    def __init__(self,name):
      self.__name= name;
    def speak(self):
        return "Meow!" 
    
def get_pet(pet='dog'):
    pets = dict(dog = Dog("hope"),cat = Cat("peace"))
    return pets[pet]

d= get_pet('cat')
print(d.speak())


