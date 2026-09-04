# 1. Arbitrary or Variable length Arguments
# 2. Positional or Required Arguments
# 3. Keyword Arguments

# Example 1: Function with Arbitrary arguments

# def sum_function(*numbers):
#     total=0
#     for i in numbers:
#         total=total+i
#     return (total)
#
# print(sum_function(10,20)) # 30
# print(sum_function(10,20,30)) # 60
# print(sum_function(100,200,300)) # 600
# print(sum_function()) # 0

# Example 2: Function with Positional and Keyword Arguments

# def myfun(i,j):
#     print(i,j)
#
# myfun(10,20) # positional arguments
# myfun(j=20,i=30) # Keyword arguments

# Example 3: Default values also can be assigned to the positional arguments
# def myfun(i=20,j=10):
#     print(i,j)
#
# myfun(100) # 100 10
# myfun() # 20 10

# Example 3: Mixing of both positional and keyword arguments

# def myfun(a,b,c):
#     print(a,b,c)

# myfun(10,20,30) # positional arguments
# myfun(a=10,b=20,c=30) # keyword arguments
# myfun(b=30,c=40,a=20) # keyword arguments
# myfun(10,20,c=30)
# myfun(10,b=20,c=30)
# myfun(10,b=20,30) # this is wrong as positional argument must appear before any keyword argument
# myfun(10,20,b=20) # this is logical error

# Example 5: Function can return multiple values

# def largest(a,b):
#     if a>b:
#         return a,b
#     elif a==b:
#         return a|b
#     else:
#         return b,a
#
# # print(largest(100,200)) # (200,100)
# res=largest(200,100)
# print(res)
# print(type(res))