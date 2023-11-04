a = 71  # Identifies 'a' as a class <int>
b = 88.44  # Identifies 'b' as a class <float>
name = "Mahar"  # Identifies 'name' as a class <str>

# to find datatype 
type(a)  # Expecting output: <class 'int'> (to find and identify the data type of 'a')
print(type(a))  # Output: <class 'int'>
c = "31"
type(c)  # Expecting output: <class 'str'> (as numbers are written in string format)
print(type(c))  # Output: <class 'str'>

# to convert one data type into another.
str(31)  # Output: '31' (converts integer 31 to string '31')
int("32")  # Output: 32 (converts string '32' to an integer)
float(32)  # Output: 32.0 (converts integer 32 to a floating-point number)

# converting string numerical to integer
d = int("32")  # Output: 32 (converts string '32' to an integer)
print(d)  # Output: 32
print(type(d))  # Output: <class 'int'> (to confirm 'd' is of type integer)

# to take input from the keyboard as a string.
name = input("Enter name: ")  # Allows the user to input their name, stored in the 'name' variable as a string
print("name is", name)  # Prints the inputted name



