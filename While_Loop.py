# While loop

# # Infinite while loop
# print("Infinite Loop:")
# while True:
#     print("This is an infinite loop")  # Output: Repeatedly prints "This is an infinite loop"
#     # Ensure a break condition to exit this loop
    

# while loop with break
print("\nLoop with Break:")
count = 0
while True:
    print(count)  # Output: Prints count from 0 to 4
    count += 1
    if count >= 5:
        break  # Exit the loop when count is equal to or greater than 5

# while loop with continue
print("\nLoop with Continue:")
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skips printing for count equal to 3
    print(count)  # Output: Prints count from 1 to 5 excluding 3

# Loop with Break and Continue
print("\nLoop with Break and Continue:")
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skips printing for count equal to 3
    if count == 4:
        break  # Exit the loop when count is 4
    print(count)  # Output: Prints count from 1 to 3 excluding 3



# List of content to display
my_list = ["apple", "banana", "cherry", "date", "fig"]

# Displaying list content using a while loop
print("Displaying list content using a while loop:")

index = 0
print(len(my_list))
while index < len(my_list):
    print(my_list[index])  # Output: Each element in the list printed on a new line
    index += 1

