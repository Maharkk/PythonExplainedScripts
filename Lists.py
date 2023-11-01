#list
a = [1,2,3,4,5,6] # This is a list
a[3] = 88  # This will change the 4 to 88 and we can change it because list is mutable object
print(a) 
print(a[2]) # Accessing list using index numbers
#print(a[6]) # This wont work because IndexError: list index out of range

# We can include different datatypes in list
b = [2,"mahar",True,7.1]
print(b)

# List slicing
friends = ["Mahar", "Surya", "Nuhman", "Safwan", "Aslam", 71]
print(friends[0:3]) # This slicing starts from 0 to 3 and will 0 to 2 of list
print(friends[-3:]) # This slicing starts from -4 and print till last of list

# List methods
l1 = [1,8,7,2,21,15]
print(l1) # as you can see the list not sorted
l1.sort() # sort function will sort the list
print(l1) # now the updated sorted list will print
#l1.reverse() # This will reverse the list
#l1.append(10) # This function will adds to the end of the list
#l1.insert(2,44) # This will insert 44 at index 2
#l1.pop(2) # This will delete the value at index 2
#l1.remove(21) # This will remove 21 from the list

# You can get all the list methods from "python docs" website



