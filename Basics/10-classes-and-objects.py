# Tutorial: http://www.learnpython.org/en/Classes_and_Objects

# Classes and Objects
# Objects are an encapsulation of variables and functions into a single entity. Objects get their variables and functions from classes. Classes are essentially a template to create your objects.
# A very basic class would look something like this:

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")
        
# We'll explain why you have to include that "self" as a parameter a little bit later. First, to assign the above class(template) to an object you would do the following:

class MyClass2:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass2()

# Now the variable "myobjectx" holds an object of the class "MyClass" that contains the variable and the function defined within the class called "MyClass".

# Accessing Object Variables
# To access the variable inside of the newly created object "myobjectx" you would do the following:

class MyClass3:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass3()

myobjectx.variable

# So for instance the below would output the string "blah":

class MyClass4:
    variable = "Hello there, my name is Max."

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass4()

print(myobjectx.variable)

# You can create multiple different objects that are of the same class(have the same variables and functions defined). However, each object contains independent copies of the variables defined in the class. For instance, if we were to define another object with the "MyClass" class and then change the string in the variable above:

class MyClass5:
    variable = "Lorem Ipsum"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass5()
myobjecty = MyClass5()

myobjecty.variable = "My name is Max."

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)

# Accessing Object Functions
# To access a function inside of an object you use notation similar to accessing a variable:

class MyClass6:
    variable = "blah"

    def function(self):
        print("This is a message, inside a function, inside a class.")

myobjectx = MyClass6()

myobjectx.function()

# Exercise
# We have a class defined for vehicles. Create two new vehicles called car1 and car2. Set car1 to be a red convertible worth $60,000.00 with a name of Fer, and car2 to be a blue van named Jump worth $10,000.00.

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
        
# your code goes here

car1 = Vehicle()
car2 = Vehicle()

car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.000

car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000.000


# test code
print(car1.description())
print(car2.description())
