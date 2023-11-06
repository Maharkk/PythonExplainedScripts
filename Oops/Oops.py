# PascalCase - EmployeeName , first letter capital
# CamelCase  - employeeName , first letter small

# Class always written in PascalCase

# Abstraction - Abstraction in action, provides an abstract method without showing its implementation
# Encapsulation - Encapsulated method, abstracts how it works internally

'''
We identify the following in our problem

Noun -> Class -> Employee

Adjective -> Attributes -> name,age,salary

Verbs -> Methods -> getSalary(), increment()
'''

# Class attribute and instance attribute

# Class definition
class Employee:
    company = "Google"  # Class attribute - specific to each class

# Instantiation - creating an instance (object) of the class
mahar = Employee()  # Object instantiation

# Accessing class attribute using the instance
print(mahar.company)  # Output: "Google"

# Changing the class attribute for all instances of the class
Employee.company = "Amazon"

# Adding instance attributes to the object
mahar.name = "Mahar"  # Instance attribute
mahar.salary = "30,000"  # Instance attribute

# Accessing instance attributes
print(mahar.name)  # Output: "Mahar"
print(mahar.company)  # Output: "Amazon" (class attribute can also be accessed through the instance)
print(mahar.salary)  # Output: "30,000"


'''
The 'self' parameter is used to refer to the instance itself, 
allowing access to its attributes and methods within the class. 
It's a way to make sure the instance itself is affected 
when modifying or accessing attributes or methods
'''

class Employee:
    company = "Google"  
    # Method to get and print the salary of an employee
    def getSalary(self):
        # Accessing and printing the company name and employee's salary
        print(f"Salary for this employee working in {self.company} is {self.salary}")

# Object instantiation
mahar = Employee()  # Creating an instance 'mahar' of the Employee class
mahar.salary = 100000
# Calling the 'getSalary' method for the 'mahar' instance
# This will print the salary and company name using instance and class attributes
mahar.getSalary()  # Output: Salary for this employee working in Google is 100000

'''Static method
Sometimes, we need a function that doesn’t use the self-parameter. We can define a static method like this:'''
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y
# Using the static method without creating an instance
result = MathOperations.add(5, 7)
print("Result of addition:", result)  # Output: Result of addition: 12


''' 
__init__() constructor
__init__() is a special method that runs as soon as the object is created.
It is known as the constructor and takes a self-argument and can also take further arguments.
For Example:'''
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
# Creating an object of the Employee class using the constructor (__init__ method)
emp1 = Employee("Alice", 30)
emp2 = Employee("Bob", 28)
# Displaying employee information using instance method
emp1.display_info()  # Output: Name: Alice, Age: 30
emp2.display_info()  # Output: Name: Bob, Age: 28



