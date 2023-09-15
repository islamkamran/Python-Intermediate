class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name:{self.name}, Age:{self.age}'
    

class Worker(Person):
    def __init__(self, name, age, salary):
        super(Worker, self).__init__(name, age)
        self.salary = salary
    
    def __str__(self):
        text = super(Worker,self).__str__()
        text += f', Salary: {self.salary}'
        return text
    
    def calc_yearly_salary(self):
        return self.salary * 12
    
worker1 = Worker('islam',26,85000)
print(worker1)
print(worker1.calc_yearly_salary())