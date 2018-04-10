class Person():
    def greet(self):
        return f'Hello {id(self)}'

if __name__ == '__main__':
    p = Person()
    print(Person.greet(p))
    print(id(p))
    print(p.greet())