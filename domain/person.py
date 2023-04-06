class Person:
    def __init__(self, name: str, age: int, id: int = None):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person(id={self.id}, name={self.name}, age={self.age})'
