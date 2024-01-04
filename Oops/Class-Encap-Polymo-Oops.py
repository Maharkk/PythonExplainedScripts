'''
1. Class:
     Think of a class as a blueprint or a recipe. It describes how to create something. 
     For example, you can have a Dog class that describes what a dog is,
     including its characteristics and actions.
 '''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking!")
#Here, Dog is a class. It has a __init__ method (constructor) 
#to set up a new dog with a name and age, and a bark method to make the dog bark.
        
"""
2. Object:
    An object is an actual instance created from a class. 
    It's like creating a specific dog using the Dog blueprint."""

my_dog = Dog(name="Buddy", age=3)

# Here, my_dog is an object of the Dog class. It has a name "Buddy" and an age of 3.
"""
3. Attributes:
     Attributes are characteristics or properties of an object. 
     In the Dog class, name and age are attributes."""
print(my_dog.name)  # Output: Buddy
# This prints the name attribute of my_dog, which is "Buddy".

"""
4. Methods:
     Methods are functions that belong to a class and can be called on objects of that class. 
     The bark method in the Dog class is an example."""
my_dog.bark()  # Output: Buddy is barking!
# This calls the bark method on my_dog, making it bark.

"""
5. Inheritance:
     Inheritance is like a family relationship. A new class can inherit the attributes 
     and methods of an existing class. For example, you can have a Poodle class that 
     inherits from the Dog class.
"""
class Poodle(Dog):
    def dance(self):
        print(f"{self.name} is dancing!")
"""
6. Encapsulation:
      Encapsulation is about bundling data and methods that operate on the data within a single 
      unit, i.e., a class. It helps in hiding the complexity."""
class Circle:
    def __init__(self, radius):
        self.__radius = radius  # Private attribute

    def get_radius(self):
        return self.__radius

    def set_radius(self, new_radius):
        if new_radius > 0:
            self.__radius = new_radius
        else:
            print("Radius must be greater than 0.")
"""
7. Polymorphism:
     Polymorphism allows you to use a common interface for different types.
      
Why is it Called Polymorphism?
    "Poly" means many, and "morph" means forms. So, polymorphism is like "many forms."
     In our example, the animal_sound function can work with many forms of animals (dog, cat, bird) 
     because they all share a common method (make_sound). 
      """
class Dog:
    def make_sound(self):
        print("Woof!")

class Cat:
    def make_sound(self):
        print("Meow!")

class Bird:
    def make_sound(self):
        print("Tweet!")
#Each class has a method called make_sound that prints the sound the animal makes
        
"""
Now, let's create a function that can make any animal sound, no matter if it's a dog, cat, or bird. 
This is where polymorphism comes into play."""

def animal_sound(animal):
    animal.make_sound()

# Creating instances of different animals
dog = Dog()
cat = Cat()
bird = Bird()

# Using the function with different animals
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
animal_sound(bird)  # Output: Tweet!

