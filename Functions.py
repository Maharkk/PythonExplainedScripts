# Function without parameters
def greet():
    print("Hello, Welcome!")

greet() # Calling the function without parameters
# Output: Hello, Welcome!


# Function with parameters
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")# Calling the function with a parameter
# Output: Hello, Alice!


# Function with default parameters
def greet_user_default(name="Guest"):
    print(f"Hello, {name}!")

# Calling the function without providing a parameter
greet_user_default()# Output: Hello, Guest!
# Calling the function with a parameter
greet_user_default("Bob") # Expected Output: Hello, Bob!



# Function with a return value
def add_numbers(a, b):
    return a + b

# Calling the function with parameters and printing the return value
result = add_numbers(5, 7)
print("Sum:", result)
# Expected Output: Sum: 12


# Function with multiple return values
def get_max_min(numbers):
    return max(numbers), min(numbers)

# Calling the function with a list and unpacking the returned values
data = [4, 9, 1, 14, 7]
max_num, min_num = get_max_min(data)
print("Maximum:", max_num)
print("Minimum:", min_num)
# Expected Output: Maximum: 14, Minimum: 1



# Recursive function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

factorial_result = factorial(5) # Calling the recursive function and printing the result
print("Factorial of 5:", factorial_result)
# Expected Output: Factorial of 5: 120


# Function to find the greatest of three numbers
def find_greatest(a, b, c):
    return max(a, b, c)
# Given numbers for finding the greatest
num1 = 10
num2 = 20
num3 = 15
# Calling the function and printing the result
result = find_greatest(num1, num2, num3)
print("The greatest number is:", result)
# Expected Output: The greatest number is: 20



# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
# Given temperature in Celsius for conversion
celsius_temp = 30
# Calling the function and printing the result
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")
# Expected Output: 30°C is equal to 86.0°F


# Function to find the sum of first 'n' natural numbers recursively
def sum_of_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_natural_numbers(n - 1)
# Given value of 'n' for sum calculation
n = 10
# Calling the function and printing the result
result = sum_of_natural_numbers(n)
print(f"Sum of first {n} natural numbers is: {result}")
# Expected Output: Sum of first 10 natural numbers is: 55



# Function to convert inches to centimeters
def inches_to_cm(inches):
    return inches * 2.54
# Given length in inches for conversion
inches = 10
# Calling the function and printing the result
centimeters = inches_to_cm(inches)
print(f"{inches} inches is equal to {centimeters} centimeters")
# Expected Output: 10 inches is equal to 25.4 centimeters


# Given text with leading and trailing spaces
text = "   Hello, this is an example   "
# Stripping the text (removing leading and trailing spaces)
stripped_text = text.strip()
# Printing the original and stripped text
print("Original Text:", text)
print("Stripped Text:", stripped_text)
# Expected Output: 
# Original Text:    Hello, this is an example   
# Stripped Text: Hello, this is an example


