class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    
    def other_activities(self, chai):
        self.chai = chai
        return self.chai
    
    # to delete an object after the work is complete
    def __del__(self):
        print("Object Deleted")

person1 = Person("islam kamran", 27)
print(person1.name, person1.age)
person1.name = "Abdullah"
print(person1.name, person1.age)

activites_person1 = person1.other_activities("Garma chai")
print(activites_person1)

del person1
