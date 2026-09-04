# creating strings in 3 approches

# Approach 1: using double quotes
# name ="John"
# grade ="B"

# Approach 2: using single quotes
# name = 'John'
# grade ='B'

# Approach 3: using constructor
# name = str() # empty string
# grade=str() # empty string

# name = str("John") # can use " or '
# grade = str("B")
# print(name,grade)
#
# print(type(name))
# print(type(grade))

# + and * operators used along with strings

# str='Welcome'
#
# print(str+" Programming") # concatinating the strings
# print(str * 3) # repeating the string value as per the number(3)

# slicing strings: slicing is extracting some portion of the string
# ending index count from 1

mystr="welcome"
print(mystr[1:3]) # el
print(mystr[:6]) #starting index is 0 by default # welcom
print(mystr[2:]) # lcome # ending index is last value

print(mystr[1:-1]) # elcom # negative index will start from end
print(mystr[1:-2]) # elco

print(mystr[-5:-2]) # lco

# Formating strings
# F string was introduced in python 3.6, and is now the preffered way of formatting strings
# To specify a string as an f-string:
# put f in front of string,and add curly braces {} as placeholders for variables and other operations

# Example 1:
# age=30
# # str="My Name is John, I am "+age # TypeError
# str=f"My Name is John, I am {age}"
# print(str)
# print(f"My Name is John, I am {age}")

# Example 2:
# Output: The price is 55

# price=55
# str = f"The Price is {price:.2f}"
# print(str)

# Example 3: performing arthematic operations inside f-string

# price=50
# str = f"The Price is {price*2} dollars"
# print(str)

# in notin with strings
# returns the boolean value

str = "Welcome"
print("come" in str) # True
print("lome" in str) # False

print("come" not in str) # False
print("lome" not in str) # True