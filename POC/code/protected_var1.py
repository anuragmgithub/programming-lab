class Person:
    def __init__(self, name):
        self.__name = name 
    
    def get_name(self):
        return self.__name  
    

person = Person("Anurag")
#print(person.__name)
print(person._Person__name) # the attribute __name in the Person class is internally renamed to _Person__name by Python.
"""
Why Name Mangling?

To make certain attributes harder to accidentally overwrite or clash when working with inheritance.
For example, if a subclass defines an attribute with the same name, it won't overwrite the parent class's mangled attribute because the names will differ.
"""