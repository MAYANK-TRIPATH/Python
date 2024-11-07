# How funtion written in Py

# def funtion ():       #this is creating a fun
#     print("Random")

# funtion()    # this is calling a fun.


#--------------------------------------------------------------------------------

# Arguments:- Information can be passed into funtion using arguments.

# def argument(argumnt):
#     print(argumnt +  " jash")

# argument("Amit")

# if dont know how many no of argument then use "*".


#--------------------------------------------------------------------------------


# Python Lambda:- A lambda function is a small anonymous function.
# It can take any no of argument but give inly ine expression.
# Mostly we use Lambda funtion when we use them as an anonymous function
#  inside another function.

# Syntax:- lambda arguments : expression

# x = lambda a: a + 10
# print(x(10))


# x = lambda a, b : a * b
# print(x(5, 10))


def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))


