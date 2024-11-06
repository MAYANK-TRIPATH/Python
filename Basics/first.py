#variables

# x = 5
# y = "Mayank"
# print(x)
# print(y)
 
# type checking
# print(type(x))
# print(type(y))

#This is called unpacking :- Extracting values into variables.
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits 
# print(x)
# print(y)
# print(z)

# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)  #this will give Pyhton is awesome

# print(x + y + z)  #this will give Pythonisawesome



#Nov-6-2024----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Variables 
# x = 5
# y = "John"
# print(x, y)


# Global Variables :- Variables declared outside the function
# x = "awesome"

# def funtion():
#     print("Pyhton is " + x)

# funtion()


# If we create a variable with same name inside a function,  this variable will be local,
#  and can only be used inside the function. The global variable with the same name will 
# remain as it was, global and with the original value.

# x = "awesome"

# def funtion():
#     x = "Okies"
#     print("Python is " + x)

# funtion()

# print("Python is " + x)


#The Global keyword :- Normally whe  you create a varibake inside a funtion it can be used inside
# only that funtion. But if you use the global keyword, the variable can be used outside the function.

def funtion():
    global x 
    x = "Checking"

funtion()
print("just " + x)

