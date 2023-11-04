# Inheritance is a way of creating a new class from an existing class.

'''
Single inheritance --->Single inheritance occurs when a child class inherits only a single parent class.
'''
# Parent class: Employee
class Employee:
    company = "Google"
    
    def showDetails(self):
        print("This is an employee")  # Method to display employee details

# Child class: Programmer (inherits from Employee)
class Programmer(Employee):
    language = "Python"  # Attribute specific to Programmer class
    #company = "Youtube" #if company is different in child class it will use chid class company over parent class 
    def getLanguage(self):
        print(f"The language is {self.language}")  # Method to display the programming language
    
    def showDetails(self):
        print("This is a programmer")  # Method to display programmer details

# Instantiating objects
e = Employee()
e.showDetails()  # Output: This is an employee

p = Programmer()
p.showDetails()  # Output: This is a programmer #if programmer class didn't had show details it will print parent class show details
print(p.company)  # Output: Google


'''
Multiple Inheritance
Multiple inheritances occurs when the child class inherits from more than one parent class.'''
# Multiple Inheritance

# Freelancer class with company and level attributes
class Freelancer:
    company = "Fiverr"  # Defines a class attribute 'company' for Freelancer class
    level = 0  # Initializes a 'level' attribute for a Freelancer
    
    def upgradeLevel(self):  # A method to upgrade the level of Freelancer
        self.level = self.level + 1

# Employee class with company and eCode attributes
class Employee:
    company = "Visa"  # Defines a class attribute 'company' for Employee class
    eCode = 120  # Defines a class attribute 'eCode' for Employee class

# Programmer class inheriting from Freelancer and Employee classes
class Programmer(Freelancer, Employee):
    name = "Mahar"  # Adds a name attribute specific to the Programmer

# Instantiates an object 'p' from the Programmer class
p = Programmer()
p.upgradeLevel()  # Calls the upgradeLevel method from the Freelancer class
print(p.level) # Output - 1
print(p.company)  # Prints the 'company' attribute from the Programmer object 'p'
# Output - fiverr
#company' from Freelancer is used due to the left-to-right search order in Python's multiple inheritance model.

'''Multilevel Inheritance
When a child class becomes a parent for another child class.
'''
class Person:
    country = "India"  # Class attribute 'country' defined for Person

    def takeBreath(self):
        print("I am breathing...")  # Method to simulate breathing


class Employee(Person):
    company = "Honda"  # Class attribute 'company' defined for Employee
    eCode = 120

    def getSalary(self):
        print(f"Salary is {self.salary}")  # Method to get the salary of an employee

    def takeBreath(self):
        print("I am an Employee so I am luckily breathing...")  # Overriding takeBreath method


class Programmer(Employee):
    company = "Fiverr"  # Class attribute 'company' redefined for Programmer

    def getSalary(self):
        print("No salary to programmers")  # Overridden method from Employee class

    def takeBreath(self):
        print("I am a Programmer so I am breathing++..")  # Overriding the takeBreath method

# Creating instances for different classes
p = Person()  # Creating an instance of the base class Person
p.takeBreath()  # Output: I am breathing...

e = Employee()  # Creating an instance of the Employee class
e.takeBreath()  # Output: I am an Employee so I am luckily breathing...
print(e.company)  # Output: Honda

pr = Programmer()  # Creating an instance of the Programmer class
pr.takeBreath()  # Output: I am a Programmer so I am breathing++..
print(pr.company)  # Output: Fiverr

