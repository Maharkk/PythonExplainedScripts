# For loop

# Printing numbers using range in a for loop
for i in range(8):
    print(i)  # Output: Prints numbers from 0 to 7


# Printing range from (start, stop) method
print("\nrange from (start, stop) method")
for i in range(3, 8):
    print(i)  # Output: Prints numbers from 3 to 7


# Printing range from (start, stop, skip) method
print("\nrange from (start, stop, skip) method")
for i in range(1, 8, 2):
    print(i)  # Output: Prints numbers from 1 to 7 skipping every other number


# Break method in a for loop
print("\nbreak method")
for i in range(8):
    print(i)
    if i == 5:
        break  # Output: Prints numbers from 0 to 5


# Continue method in a for loop
print("\ncontinue method")
for i in range(8):
    if i == 5:
        continue
    print(i)  # Output: Prints numbers from 0 to 7 excluding 5


# Loop with else and pass
for i in range(5):
    print(i)  # Output: Prints numbers from 0 to 4
else:
    print("Loop completed without a 'break'")  # Output: Loop completed without a 'break'

for j in range(3):
    if j == 2:
        pass  # Placeholder, does nothing
    print(j)  # Output: Prints numbers 0 to 2


# Displaying list content using a for loop
my_list = ["apple", "banana", "cherry", "date", "fig"]
print("Displaying list content using a for loop:")
for item in my_list:
    print(item)  # Output: Prints each item in the list on a new line


# Multiplication table for a number using a for loop
number = 7
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")  # Output: Prints multiplication table for 7 from 1 to 10


# Finding prime numbers within a range using a for loop
start = 10
end = 30
print(f"Prime numbers between {start} and {end}:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)  # Output: Prints prime numbers between 10 and 30


# Sum of n natural numbers using a for loop
n = 10
sum_n = 0
for i in range(1, n + 1):
    sum_n += i
print(f"Sum of first {n} natural numbers: {sum_n}")  # Output: Prints the sum of first 10 natural numbers


# Section 1: Greeting names starting with "S"
names = ["Harry", "Sohan", "Sachin", "Rahul"]
for name in names:
    if name.startswith("S"):
        print("Hello " + name)
# Expected Output:
# Hello Sohan
# Hello Sachin


# Section 2: Calculate factorial of a number
num = int(input("Enter the number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is {factorial}")
# Expected Output:
# (Depends on the number entered by the user)


# Section 3: Printing a diamond pattern
n = 3
for i in range(n):
    print(" " * (n - i - 1), end="")
    print((2 * i + 1) * "*", end="")
    print(" " * (n - i - 1))
# Expected Output:
#   *
#  ***
# *****
