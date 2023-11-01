# Dictionary is a collection of key-value pairs
# Mutable
myDict = {
    "fast": "In a Quick Manner", 
    "mahar": "A Coder",
    "marks": [1, 2, 5],  # "fast, mahar, marks" are keys and their corresponding values are "In a Quick Manner, A Coder, [1, 2, 5]"
    "anotherdict": {'ronaldo': 'Player'}  # Nested dictionary inside myDict
} 

print(myDict['fast'])  # Access value by 'fast' key
print(myDict['mahar'])  # Access value by 'mahar' key

# Update the value of 'marks'
myDict['marks'] = [45, 78]
print(myDict['marks'])  # Print the updated 'marks' value

# Access nested dictionary value using 'ronaldo' key inside 'anotherdict'
print(myDict['anotherdict']['ronaldo'])

# Dictionary Methods
print(myDict.keys())  # Display all keys in the dictionary
print(myDict.values())  # Display all values in the dictionary
print(type(myDict.keys()))  # Display the data type of keys, which is 'dict_keys'
print(list(myDict.keys()))  # Convert keys to a list for easier manipulation
print(myDict.items())  # Display key-value pairs in tuple form for all contents in the dictionary

# Update the dictionary by adding key-value pairs from updateDict
updateDict = {"ck": "friend"}
myDict.update(updateDict)  #update the dictionary by adding key-value pairs from updateDict
print(myDict)

# Difference between .get() and normal dictionary key access
print(myDict.get("ck"))  # Output will be 'friend'
print(myDict.get("ck2"))  # Output will be 'None', as 'ck2' key doesn't exist
print(myDict["ck"])  # output will be 'friend'
#print(myDict["ck2"]) # The following line will raise a KeyError as 'ck2' key doesn't exist

