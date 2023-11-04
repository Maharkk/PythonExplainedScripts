'''
Create a class programmer for storing information of a few programmers working at Microsoft.'''

class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")

mahar = Programmer("Mahar", "Skype")
kevin = Programmer("Kevin", "GitHub")  # Changed alka to kevin
mahar.getInfo()  # Output: The name of the Microsoft programmer is Mahar and the product is Skype
kevin.getInfo()  # Output: The name of the Microsoft programmer is Kevin and the product is GitHub


'''
write a class calculator capable of finding square, cube, and the square root of a number.
'''
class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The value of {self.number} square is {self.number ** 2}")

    def squareRoot(self):
        print(f"The value of {self.number} square root is {self.number ** 0.5}")

    def cube(self):
        print(f"The value of {self.number} cube is {self.number ** 3}")

a = Calculator(9)
a.square()       # Output: The value of 9 square is 81
a.squareRoot()   # Output: The value of 9 square root is 3.0
a.cube()         # Output: The value of 9 cube is 729



'''Write a class Train which has methods to book a ticket, get status(no of seats), 
and get fare information of trains running under Indian Railways.
'''
class Train:
    def __init__(self, name, fare, seats):
        # Initialize instance attributes
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        # Display train status
        print("************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print("************")

    def fareInfo(self):
        # Display fare information
        print(f"The price of the ticket is: Rs {self.fare}")

    def bookTicket(self):
        # Book a ticket if seats are available
        if self.seats > 0:
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats -= 1  # Reduce available seats
        else:
            print("Sorry, this train is full! Kindly try in tatkal")

    def cancelTicket(self, seatNo):
        pass  # To be implemented for canceling tickets

# Create an instance and perform operations
intercity = Train("Intercity Express: 14015", 90, 2)
intercity.getStatus()  # Output: The name and available seats of the train
intercity.bookTicket()  # Output: Successful ticket booking with seat number
intercity.bookTicket()  # Output: Successful ticket booking with seat number
intercity.bookTicket()  # Output: The train is full message
intercity.getStatus()  # Output: Updated available seats after bookings


'''Can you change the self parameter inside a class to something else (say 'mahar')? 
Try changing self to 'slf' or 'mahar' and see the effects'''
class Sample:
    def __init__(slf, name):
        slf.name = name

obj = Sample("mahar")
print(obj.name) # no proble, ypu can change but its better to use self

