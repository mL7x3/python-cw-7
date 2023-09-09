class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'My name is {self.name} and I am {self.age} years old '
    def is_adult(self):
        if self.age > 18:
            print('You have too much responsibilities')
        else:
            print('Lucky')

first_person = Person('mubarak', 15)
print(first_person)
first_person.is_adult()