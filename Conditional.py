# if
# elif
# else

#Example 1: Only if statement
x = 15

if x > 10:  # If condition: Check if x is greater than 10
    print("x is greater than 10")  # Output: "x is greater than 10"
else:
    print("x is less than or equal to 10")  # Output: This line won't be executed in this case

#Example 2: if and elif statements
y = 7

if y > 10:  # If condition: Check if y is greater than 10
    print("y is greater than 10")  # Output: This line won't be executed in this case
elif y == 10:  # Elif condition: Check if y is equal to 10
    print("y is equal to 10")  # Output: This line won't be executed in this case
else:
    print("y is less than 10")  # Output: "y is less than 10"


#Example 3: Nested if and else statements
z = 5

if z < 10:  # If condition: Check if z is less than 10
    print("z is less than 10")  # Output: "z is less than 10"

    if z % 2 == 0:  # Nested If condition: Check if z is an even number
        print("z is an even number")  # Output: This line won't be executed in this case
    else:
        print("z is an odd number")  # Output: "z is an odd number"
else:
    print("z is 10 or greater")  # Output: This line won't be executed in this case


# Relational Operators
x = 10
y = 5

if x > y:
    print("x is greater than y")  # Output: "x is greater than y"
elif x == y:
    print("x is equal to y")  # Output: This line won't be executed in this case
elif x != y:
    print("x is not equal to y")  # Output: "x is not equal to y"
elif x >= y:
    print("x is greater than or equal to y")  # Output: This line won't be executed in this case
elif x < y:
    print("x is less than y")  # Output: This line won't be executed in this case
else:
    print("x is not a integer")

# Logical Operators
p = True
q = False

if p and q:
    print("Both p and q are True")  # Output: This line won't be executed in this case
elif p or q:
    print("At least one of p or q is True")  # Output: "At least one of p or q is True"
elif not p:
    print("p is False")  # Output: This line won't be executed in this case
elif not q:
    print("q is False")  # Output: "q is False"
else:
    print("something is not right")


# Using 'in' and 'is' operators
a = [1, 2, 3]
b = [1, 2, 3]
c = a

if 2 in a:
    print("2 is in list a")  # Output: "2 is in list a"
elif b is a:
    print("b is the same object as a")  # Output: This line won't be executed in this case
elif c is a:
    print("c is the same object as a")  # Output: "c is the same object as a"
else:
    print("None of the conditions are True")  # Output: This line won't be executed in this case
