# Example 1: print 1 to 10 using for loop
# range(1,11)
from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

# for i in range(1,11):
#     print(i)

# Example 2: print even numbers between 1 to 10

# Method 1:
# for i in range(2,11,2):
#     print(i)

# # Method 2:
# for i in range(0,11):
#     if i%2==0:
#         print(i)

# Method 3:
# for i in range(0,11,2):
#     if i%2==0:
#         print(i,"is an Even number")
#     else:print(i,"is an Odd number")

# Example 3: print in reverse order
# range(10,0,-1)
# for i in range(10,0,-1):
#     print(i)

# Example 4: in python loop variables are accessible outside the for loop after loop ends
# for i in range(1,6):
#     print(i)
# print(i)

# Example 5:
for i in range(1,6):
    pass
print(i) # 5

