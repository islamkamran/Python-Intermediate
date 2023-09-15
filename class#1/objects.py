class Person:
    # class variables
    amount = 0

    def __init__(self, name,age):
        self.name = name
        self.age = age
        # self is for accessing the data inside of the function to access data inside of the class we write the class name in this case to access amount
        Person.amount += 1

    # to delete an object after the work is complete
    def __del__(self):
        Person.amount -= 1


    # def other_activities(self, chai):
    #     self.chai = chai
    #     return self.chai
    
    def __str__(self):
        return f'Name: {self.name}, Age:{self.age}'
    

person1 = Person("islam kamran", 27)
print(person1)
person2 = Person("Arsalan", 28)
print(Person.amount)
print(person2)
del person2
print(Person.amount)

