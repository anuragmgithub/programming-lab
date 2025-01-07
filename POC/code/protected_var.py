class Person:
    def __init__(self, name):
        self._name = name   # Internal or protected attribute 
    
    @property
    def get_name(self):
        return self._name
    
person = Person("Anurag")
print(person._name)   #still accessible, but discouraged
print(person.get_name)
