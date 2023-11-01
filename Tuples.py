#Tuples 
#Tuples are immutable and created using parentheses () 
#while lists are mutable and use square brackets []. 

t = (1, 2, 3, 4, 5, 3)
print(t)  # Output: (1, 2, 3, 4, 5, 3)
print(t[2])  # Output: 3 (Accesses the element at index 2)

# t[2] = 44  # This line is commented out because it won't work due to immutability

t1 = ()  # Creates an empty tuple
t2 = (1,)  # To create a single-element tuple, a comma is necessary
#t2 = (1) # This wont create a single element tuple

# Tuples method
print(t.count(3))  # Output: 2 (Returns the number of occurrences of the element 3 in the tuple 't')
print(t.index(5))  # Output: 4 (Returns the index of the first occurrence of the element 5 in the tuple)

t4 = (3, "harry", True, 7.4)  # A tuple can include any data type
print(t4)  # Output: (3, 'harry', True, 7.4)

