



class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


zhang = Student('zhangweilin', 100)
zhang.print_score()


#继承与多态
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')

a = Animal()
b = Dog()
print(isinstance(b,Animal)) # True
print(isinstance(a,Dog))  # False 只能向上兼容

def run_twice(animal):
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

import sys
n = 0
word = []

for line in open('a.txt','r'):
    word.append(line.split(' '))
    print(line)
    n+=1