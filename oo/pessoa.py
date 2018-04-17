class Person():
    eyes = 2

    def __init__(self,*sons, name=None, age=0):
        self.age = age
        self.name = name
        self.sons = list(sons)

    def greet(self):
        return f'Hello {id(self)}'


    @staticmethod
    def static_method():
        return 42

    @classmethod
    def class_method(cls):
        return f'{cls} - {cls.eyes}'

if __name__ == '__main__':
    bruno = Person(name = 'Bruno')

    vinicius = Person(name = 'Vinicius')

    valeria = Person(vinicius,bruno,name = 'Valeria')

    for sons in valeria.sons:

        print(sons.name)

    valeria.lastName = 'silva'
    print(valeria.lastName)
    print(valeria.__dict__)

    del valeria.lastName

    valeria.eyes = 1
    del valeria.eyes

    print(valeria.__dict__)
    print(bruno.__dict__)

    Person.eyes = 3
    print(Person.eyes)
    print(valeria.eyes)
    print(bruno.eyes)
    print(id(Person.eyes),id(valeria.eyes),id(bruno.eyes))
    print(Person.static_method(),valeria.static_method())
    print(Person.class_method(), valeria.class_method())