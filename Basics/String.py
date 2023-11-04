b = 'Mahar'  # Define a string variable 'b' containing the text 'Mahar'. Single quotes are used.
c = "Mahar's"  # Define a string variable 'c' containing the text 'Mahar's'. Double quotes are used to include a single quote within the string.
d = '''Mahar
Hassain kk'''  # Define a string variable 'd' with multi-line text using triple quotes.

# Print the values of variables b, c, and d
print(b)  # Output: Mahar
print(c)  # Output: Mahar's
print(d)  # Output: Prints multi-line text:
         # Mahar
         # Hassain kk

# Print the types of the variables b, c, and d using the 'type()' function
print(type(b), type(c), type(d))  # Output: <class 'str'> <class 'str'> <class 'str'>

#------------------------------------------------------------

# String slicing and concatenation example
greetings = "Good Morning, "  # Define a string variable 'greetings' containing "Good Morning, "
name = "mahar"  # Define a string variable 'name' containing "mahar"

# Print the type of the variable 'name' using the 'type()' function
print(type(name))  # Output: <class 'str'>

# Access and print individual characters in the 'name' string
print(name[0])  # Output: 'm' (the first character of the string)
print(name[4])  # Output: 'r' (the fifth character of the string, indexing starts at 0)

# Performing string slicing to extract specific portions of the 'name' string
print(name[0:3])  # Output: 'mah' (characters from index 0 to index 2)
print(name[1:4])  # Output: 'aha' (characters from index 1 to index 3)

# Attempting to access an index out of range would result in an error
# print(name[5])  # This line is commented out to prevent an IndexError

# Concatenating two strings and printing the combined result
print(greetings + name)  # Output: 'Good Morning, mahar'
# Or, we can use a separate variable to store the concatenated string and then print it
# x = greetings + name
# print(x)

# Slicing with skip value
# The syntax for slicing is [start:stop:step]
ad = name[0:5:2]  # Output: "mhr"
# ad = name[0:5:1]  # Output: "mahar"
# ad = name[0:5:3]  # Output: "ma"
# ad = name[0:4:2]  # Output: "mr"
print(ad)





