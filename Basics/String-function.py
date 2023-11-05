Story = "Once upon a time there was a programmer named Mahar who learned python from youtube"

# String Functions
print(len(Story))  # Output: 76
# The len() function returns the number of characters in the 'Story' string.
print(Story.endswith("youtube"))  # Output: True
print(Story.endswith("from"))  # Output: False
print(Story.count("a"))  # Output: 7
print(Story.count("was"))  # Output: 1
print(Story.capitalize())  # Output: "Once upon a time there was a programmer named mahar who learned python from youtube"
print(Story.find("Mahar"))  # Output: 41
print(Story.find("upon"))  # Output: 5
print(Story.replace("Mahar", "Mahar Hassain KK"))  # Output: "Once upon a time there was a programmer named Mahar Hassain KK who learned python from youtube"

# Escape Sequences
a = "Mahar is good. He is not that good."
print(a) # Output: "Mahar is good. He is not that good."

# a = "Mahar is good. 
#He is not that good." we can't make like this with rest on next line

b = '''Mahar is good. 
He is not that good.'''
print(b) # Output: It will display two lines, separating "He is not that good." to the next line

c = "Mahar is good. \nHe is not that good."
print(c)  # Output: It will display two lines, separating "He is not that good." to the next line due to '\n'.

# We can use the "b" way or "c" way to display two lines.