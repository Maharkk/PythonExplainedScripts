#list
a = [1, 2, 3, 4, 5, 6]  # This is a list
a[3] = 88  # Changes the value at index 3 (4th element) to 88
print(a)  # Output: [1, 2, 3, 88, 5, 6]
print(a[2])  # Output: 3 (Accesses the value at index 2)
#print(a[6]) # This wont work because IndexError: list index out of range

b = [2, "mahar", True, 7.1]  # A list can include different data types
print(b)  # Output: [2, 'mahar', True, 7.1]

# List slicing
friends = ["Mahar", "Surya", "Nuhman", "Safwan", "Aslam", 71]
print(friends[0:3])  # Output: ['Mahar', 'Surya', 'Nuhman'] (Slices elements at index 0 to index 2)
print(friends[-3:])  # Output: ['Safwan', 'Aslam', 71] (Slices last 3 elements)

# List methods
l1 = [1, 8, 7, 2, 21, 15]
print(l1)  # Output: [1, 8, 7, 2, 21, 15]
l1.sort()  # Sorts the list
print(l1)  # Output: [1, 2, 7, 8, 15, 21] (Sorted list)
# Uncomment and test the following methods one at a time to see their effects:
# l1.reverse()  # Reverses the list
# l1.append(10)  # Adds 10 to the end of the list
# l1.insert(2, 44)  # Inserts 44 at index 2
# l1.pop(2)  # Removes the value at index 2
# l1.remove(21)  # Removes the first occurrence of value 21 from the list

# You can get all the list methods from "python docs" website



