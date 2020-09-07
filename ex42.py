# is-a , has-a
class Animal(object):
    pass

## is-a
class Dog(Animal):

    def __init__(self, name):
        ## has-a
        print(f"Creating Dog object: {name}....")
        self.name = name

# is-a
class Cat(Animal):

    def __init__(self, name):
        ## has-a
        print(f"Creating Cat object: {name}....")
        self.name = name

# is-a
class Person():

    def __init__(self, name):
        ## has-a
        print(f"Creating Person object: {name}....")
        self.name = name

        ## Perxxx
        self.pet = None

# is-a
class Employee(Person):

    def __init__(self, name, salary):
        print(f"Creating Employee object: {name}....")
        ## Explicit call parent class constructor to setup 'name' attribute
        super(Employee, self).__init__(name)
        # has-a
        self.salary = salary

## is-a
class Fish(object):
    pass

## is-a
class Salmon(Fish):
    pass

# is-a
class Halibut(Fish):
    pass


# rover
rover = Dog("Rover")

## is-a
satan = Cat("Satan")

# is-a
mary = Person("Mary")

# has-a
mary.pet = satan

#is-a
frank = Employee("Frank", 120000)

# has-a
frank.pet = rover

#is-a
flipper = Fish()

# is-a
crouse = Salmon()

# is-a
harry = Halibut()
