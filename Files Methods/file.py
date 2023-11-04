# Modes of opening a file
# r – open for reading
# w – open for writing
# a – open for appending
# + -> open for updating
# ‘rb’ will open for read in binary mode
# ‘rt’ will open for read in text mode


# Reading file contents
x = open("sample.txt", "r") # we can use single or double inverted comma's here
#open is a built in function
# by default its on "r" and ists not mandatory to mention id you want write or "w" then its mandatory
data = x.read()
#data = x.read(5) # to read first 5 characters
print(data)
x.close # its better to close the file after functions used

print("\nreadline method shown below\n")
x = open("sample.txt", "r")
data = x.readline() # to print first line
print(data)
data = x.readline() # to print second line
print(data)
x.close

# Writing to a file
f = open("writingfile.txt", "w")
f.write("here am writing a file ") # Can be called multiple times
# am writing a file and without a file present at the stage but it will write and save in a new created file
f.close()

# Appending to a file
f = open("writingfile.txt", "a")
f.write("here am appending a file ") # if called multiple times it will append multiple times
f.close()


# using with opening a file and read and write
with open("sample.txt") as y:
    y.read()
with open("sample.txt", "w") as y:
    y.write("with option testing")

# There is no need to write f.close() as it is done automatically