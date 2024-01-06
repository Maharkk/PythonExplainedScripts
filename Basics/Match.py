def identify_value(value):
    match value:
        case 0:
            print("It's zero")
        case 1:
            print("It's one")
        case "hello":
            print("It's the string 'hello'")
        case _: # '_' Default case
            print("It's something else")

# Test cases
identify_value(0)        # Output: It's zero
identify_value(1)        # Output: It's one
identify_value("hello")  # Output: It's the string 'hello'
identify_value(3.14)     # Output: It's something else
