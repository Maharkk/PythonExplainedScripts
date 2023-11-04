'''
Q1 Create a class C-2d vector and use it to 
  create another class representing a 3-d vector.
'''
class C2dVector:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"


class C3dVector(C2dVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

v2d = C2dVector(3, 4)
v3d = C3dVector(3, 4, 5)
print(v2d)  # Output: 3i + 4j
print(v3d)  # Output: 3i + 4j + 5k


'''
Q2 Create a class of pets from a class Animals and 
   further create class Dog from Pets. Add a method bark to class Dog.
'''
class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    def bark(self):
        return "Woof!"

dog = Dog()
print(dog.bark())  # Output: Woof!


''' 
Q3 Create a class Employee and add salary and increment properties to it.
   Write a method SalaryAfterIncrement method with a @property decorator 
   with a setter which changes the value of increment based on the salary.
'''
class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment

    @property
    def SalaryAfterIncrement(self):
        return self.salary * self.increment

    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self, new_increment):
        self.increment = new_increment / self.salary

emp = Employee(50000, 1.05)
print(emp.SalaryAfterIncrement)  # Output: 52500.0
emp.SalaryAfterIncrement = 1.10
print(emp.SalaryAfterIncrement)  # Output: 55000.0



''' 
Q4 Write a class complex to represent complex numbers, along with 
   overloaded operators + and * which adds and multiplies them.
'''
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.imag * other.real + self.real * other.imag)

c1 = Complex(3, 4)
c2 = Complex(2, 5)
add_result = c1 + c2
mul_result = c1 * c2
print(f"Addition: {add_result.real} + {add_result.imag}i")  # Output: Addition: 5 + 9i
print(f"Multiplication: {mul_result.real} + {mul_result.imag}i")  # Output: Multiplication: -14 + 23i


'''
Q5  Write a class vector representing a vector of n dimension. 
    Overload the + and * operator which calculates the sum and the dot product of them.
'''
class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        return " + ".join([f"{self.vec[i]}{chr(105 + i)}" for i in range(len(self.vec))])

    def __add__(self, vec2):
        new_vec = [self.vec[i] + vec2.vec[i] for i in range(len(self.vec))]
        return Vector(new_vec)

    def __mul__(self, vec2):
        new_vec = [self.vec[i] * vec2.vec[i] for i in range(len(self.vec))]
        return sum(new_vec)

    def __len__(self):
        return len(self.vec)

v1 = Vector([4, 7, 10])
v2 = Vector([2, 3, 5])
v3 = v1 + v2
dot_product = v1 * v2
print(v1)  # Output: 4i + 7j + 10k
print(len(v1))  # Output: 3
print(v3)  # Output: 6i + 10j + 15k
print(dot_product)  # Output: 63

"""
Q6 Write __str__() method to print the vector as follows:
   7i + 8j + 10k
"""
class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        dim = ["i", "j", "k"]
        result = " + ".join([f"{self.vec[i]}{dim[i]}" for i in range(len(self.vec))])
        return result

    def __add__(self, vec2):
        new_vec = [self.vec[i] + vec2.vec[i] for i in range(len(self.vec))]
        return Vector(new_vec)

    def __mul__(self, vec2):
        new_vec = [self.vec[i] * vec2.vec[i] for i in range(len(self.vec))]
        return sum(new_vec)

    def __len__(self):
        return len(self.vec)

v1 = Vector([7, 8, 10])
v2 = Vector([2, 3, 5])
v3 = v1 + v2
dot_product = v1 * v2
print(v1)  # Output: 7i + 8j + 10k
print(len(v1))  # Output: 3
print(v3)  # Output: 9i + 11j + 15k
print(dot_product)  # Output: 104

'''
Q7  Override the __len__() method on vector of 
    problem 5 to display the dimension of the vector.
'''
class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        dim = ["i", "j", "k"]
        result = " + ".join([f"{self.vec[i]}{dim[i]}" for i in range(len(self.vec))])
        return result

    def __add__(self, vec2):
        new_vec = [self.vec[i] + vec2.vec[i] for i in range(len(self.vec))]
        return Vector(new_vec)

    def __mul__(self, vec2):
        new_vec = [self.vec[i] * vec2.vec[i] for i in range(len(self.vec))]
        return sum(new_vec)

    def __len__(self):
        return len(self.vec)

    def dimension(self):
        return f"Dimension of the vector is {len(self.vec)}"

v1 = Vector([7, 8, 10])
v2 = Vector([2, 3, 5])
v3 = v1 + v2
dot_product = v1 * v2
print(v1)  # Output: 7i + 8j + 10k
print(len(v1))  # Output: 3
print(v3)  # Output: 9i + 11j + 15k
print(dot_product)  # Output: 104
print(v1.dimension())  # Output: Dimension of the vector is 3
