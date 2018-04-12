class Person():
    def __init__(self, name=None, age=0):
        self.age = age
        self.name = name

    def greet(self):
        return f'Hello {id(self)}'

if __name__ == '__main__':
    p = Person('Bruno')
    print(Person.greet(p))
    print(id(p))
    print(p.greet())
    print(p.name)
    p.name = 'Bruno Falis'
    print(p.name)