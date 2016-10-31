# coding:utf-8
class Animal(object):
    def __init__(self):
        pass

    def run(self):
        print 'animal is run'


class Dog(Animal):
    def run(self):
        print 'dog is run'


class Cat(Animal):
    def run(self):
        print 'cat is run'

animal = Animal()
animal.run()
dog = Dog()
dog.run()
cat = Cat()
cat.run()

print isinstance(dog, Animal)
print isinstance(cat, Dog)
print isinstance(cat, Cat)

print type(dog)
print type(cat)

if type(dog) == type(animal):
    print 'yes'
else:
    print 'no'







