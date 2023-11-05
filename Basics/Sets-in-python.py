# Sets is a collection of non-repetitive contents
# Unordered
# Unindexed
# Immutable

a = {1, 2, 3, 4, 1}
print(a)  # Output: {1, 2, 3, 4} - It will not include the last '1' in sets because sets do not allow duplicates
print(type(a))  # Output: <class 'set'>

b = {}  # This syntax will create an empty dictionary, not an empty set
print(b)  # Output: {} - An empty dictionary
print(type(b))  # Output: <class 'dict'>

# To create an empty set, use this syntax
c = set()
print(c)  # Output: set()
print(type(c))  # Output: <class 'set'>

# Set methods
c.add(4)  # Adds content to a set
c.add(3)
c.add(4)  # Adding '4' again, but sets do not allow duplicates, so it will only display '4' once
# c.add([1, 2])  # We cannot add a list or dictionary into a set as they are mutable objects
c.add((6, 7))  # We can add a tuple to a set
print(c)  # Output: {3, 4, (6, 7)} - The set after addition

# Length of a set
print(len(c))  # Prints the length of the set
print(c)  # Output: {3, 4, (6, 7)} - Current set

# To remove an item from the set
c.remove(3)  # Removes '3' from set 'c'
print(c)  # Output: {4, (6, 7)} - Set after removing '3'
