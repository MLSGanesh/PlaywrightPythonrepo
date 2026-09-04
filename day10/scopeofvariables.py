# Global and local variables
# Variables created outside of the function are called global variables
# Variables created inside of the function are called local variables

# Example 1:
# x=20 # global variable
#
# def myfun():
#     y=10 # local variable
    # print(x) # able to access global variable inside the function
    # print(y)
# myfun()

# print(x)
# print(y) # type error, as local variable cannot be accessed outside the function

# Example 2:
# x=100 # global variable
# def myfun():
#     x=200 # local variable
#     print(x) # 200
#
# myfun()
#
# print(x) # 100

# Example 3: updating the global variable value inside the function
# x=100 # global variable
# def myfun():
#     global x
#     x=200
#     print(x)
#
# myfun()
# print(x)

# Example 4: Also can declare global variable inside the function

# def myfun():
#     # global x = 100 # invalid syntax
#     global x
#     x = 200
#     print(x)
#
# myfun()
# print(x)

# celsius = float(25)
#
# fahrenheit = celsius * 9 / 5 + 32
#
# print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")