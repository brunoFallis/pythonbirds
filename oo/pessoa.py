class Person():
    def __init__(self,*sons, name=None, age=0):
        self.age = age
        self.name = name
        self.sons = list(sons)

    def greet(self):
        return f'Hello {id(self)}'

if __name__ == '__main__':
    bruno = Person(name = 'Bruno')

    vinicius = Person(name = 'Vinicius')

    valeria = Person(vinicius,bruno,name = 'Valeria')

    for sons in valeria.sons:

        print(sons.name)