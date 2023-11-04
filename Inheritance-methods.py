"""
Super() method
Super method is used to access the methods of a superclass in the derived class"""
class Vehicle:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def start_engine(self):
        print("Engine started!")


class Car(Vehicle):
    def __init__(self, name, year, model):
        super().__init__(name, year)  # Using super() to call the __init__() method of the Vehicle class
        self.model = model

    def start_engine(self):
        super().start_engine()  # Using super() to call the start_engine() method of the Vehicle class
        print(f"{self.name} {self.model}'s engine has started.")


# Creating an instance of the Car class
my_car = Car("Toyota", 2022, "Corolla")

# Calling the start_engine() method from the Car class
my_car.start_engine() 
# output
# Engine started!
# Toyota Corolla's engine has started.


'''
Class methods
A class method is a method which is bound to the class and not the object of the class.
@classmethod decorator is used to create a class method.'''

class Employee:
    company = "Camel"  # Class variable to store the company name
    salary = 100  # Class variable to store the default salary
    location = "Delhi"  # Class variable to store the default location

    # Alternative method to change the salary using a different syntax, but it's currently commented out.
    # def changeSalary(self, sal):
    #     self.__class__.salary = sal

    @classmethod
    def changeSalary(cls, sal):
        # Class method to change the salary for all instances of the class
        cls.salary = sal

# Creating an Employee object
e = Employee()

print(e.salary)  # Output: 100
# Displays the default salary value before the change

# Changing the salary using the class method
e.changeSalary(455)

print(e.salary)  # Output: 455
# Shows the salary after the change made through the class method

print(Employee.salary)  # Output: 455
# Outputs the updated salary value accessed directly from the class


'''#@property decorators
#@.getters and @.setters
#Getter Method: The method decorated with @property acts as a getter. 
                It facilitates the retrieval of a property's value. 
                It is accessed without calling the method, making it m
                ore intuitive and readable.

#Setter Method: When you use the @<attribute>.setter decorator, 
                it allows you to define a method that is invoked 
                whenever you try to set the value of the property. 
                This provides a way to control the setting of attributes 
                and perform additional operations or checks before assigning a new value.

#The method name with @property decorator is called getter method.'''

# This is  example one for above method
class Employee:
    company = "Bharat Gas"  # Class attribute representing the company name
    salary = 5600  # Base salary attribute for the employee
    salarybonus = 400  # Salary bonus attribute for the employee

    # @property decorator to create a getter method for total salary calculation
    @property
    def totalSalary(self):
        return self.salary + self.salarybonus  # Calculate the total salary as the sum of base salary and bonus

    # @totalSalary.setter decorator to create a setter method for total salary modification
    @totalSalary.setter
    def totalSalary(self, val):
        # Validate if the provided total salary is less than the base salary to prevent negative total salary
        if val < self.salary:
            raise ValueError("Total salary cannot be less than the base salary.")
        
        # Calculate and update the salarybonus and salary based on the provided total salary
        self.salarybonus = val - self.salary  # Update the bonus as the difference between total salary and base salary
        self.salary = val - self.salarybonus  # Update the base salary based on the provided total salary

# Instantiate an Employee object
e = Employee()

# Output the total salary of the employee using the property decorator
print(e.totalSalary)  # Output: 6000 (5600 salary + 400 salary bonus)

# Set the total salary of the employee using the setter method
e.totalSalary = 5800

# Output the adjusted base salary and salary bonus after modifying the total salary
print(e.salary)  # Output: 5400 (adjusted salary value)
print(e.salarybonus)  # Output: 400 (adjusted salary bonus value)

# ----- 2nd Example ---------
class Circle:
    def __init__(self, radius):
        self._radius = radius  # Prefixing with an underscore indicates it as a private variable

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive.")
        self._radius = value

# Using the Circle class
c = Circle(5)
print(c.radius)  # Output: 5

c.radius = 10  # Calls the radius setter method
print(c.radius)  # Output: 10

#c.radius = -3  # Trying to set an invalid negative radius value
# Raises a ValueError: "Radius must be positive."



'''
Operator Overloading in Python
Operator overloading is a feature in Python 
  that allows the same operator to have 
  different meanings in different contexts.
'''
# Operator Overloading Example: Overloading +, -, *

class MyNumber:
    def __init__(self, number):
        self.number = number

    # Overloading the addition operator (+)
    def __add__(self, other):
        return self.number + other.number

    # Overloading the subtraction operator (-)
    def __sub__(self, other):
        return self.number - other.number

    # Overloading the multiplication operator (*)
    def __mul__(self, other):
        return self.number * other.number

# Instantiate MyNumber objects
num1 = MyNumber(5)
num2 = MyNumber(10)

# Overloaded operators: +, -, *
result_add = num1 + num2
result_sub = num1 - num2
result_mul = num1 * num2

print("Result of num1 + num2:", result_add)  # Output: 15
print("Result of num1 - num2:", result_sub)  # Output: -5
print("Result of num1 * num2:", result_mul)  # Output: 50



