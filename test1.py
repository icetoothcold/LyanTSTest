class Animal(object):
	def run(self):
		print 'Animal is running...'

class Dog(Animal):
        def run(self):
                print 'Dog is running...'

class Cat(Animal):
        def run(self):
                print 'Cat is running...'

class Tortoise(Animal):
        def run(self):
                print 'Tortoise is running slowly'

def run_twice(animal):
        animal.run()
        animal.run()

dog=Dog()
cat=Cat()
tortoise=Tortoise()

dog.run()
cat.run()

run_twice(dog)
run_twice(cat)
run_twice(tortoise)

a=type(dog)
b=type(123)

print a,b
