# capitalize()

# s="hello"
# print(s.capitalize())

# casefold() and lower(): converts string to lowercase
# s="Hello"
# print(s.casefold()) #
# print(s.lower()) # hello

# upper(): converts string to uppercase
# s="Hello"
# print(s.upper()) # HELLO

# title() converts first character of each word to upper case
# s="welcome to python"
# print(s.title())

# swapcase() it converts lower case to upper case and vice versa
# s="welcome TO pYTHON"
# print(s.swapcase())

# center(): Returns a centered string
# str = "banana"
# print(str.center(10))
# print(str.center(10,'*')) # **banana**

# format(): formats specified values in a string
# name="John"
# print("Hello {}".format(name)) # Hello John

# find(): searches for specified values in a string and returns the position of it
# s="Hello"
# print(s.find("e")) # 1
# print(s.find("l")) # 2
# print(s.find("x")) # -1 value is not found

# index(): searches for specified values in a string and returns the position of it.
# same as find() but raises a ValueError if the value if not found.
# s="Hello"
# print(s.index("e")) # 1
# print(s.index("l")) # 2
# print(s.index("x")) # ValueError

# count(): returns number of times a specified value repeated in a string
# s="banana"
# print(s.count("a")) # 3
# print(s.count("na")) #2

# replace(): returns a string where the specified value is replaced with specified value
# s="Hello World"
# print(s.replace("World", "There"))
# print(s.replace("l", "R"))

# isalnum(): returns True if all characters in the string are alphanumeric (no punctuation or spaces).
# s="ABC123"
# print(s.isalnum()) # True
#
# s="ABC!"
# print(s.isalnum()) # False

# isalpha(): returns True if all characters in the string are alphabets

# s="Hello"
# print(s.isalpha()) # True
# s="123"
# print(s.isalpha()) # False

# isdecimal(): returns True if all characters in the string are decimals (0-9)
# s="123"
# print(s.isdecimal()) # True
#
# s="123.45"
# print(s.isdecimal()) # False
#
# s="XYZ"
# print(s.isdecimal()) # False

# isdigit(): returns True if all characters are digits
# s="123"
# print(s.isdigit()) # True
#
# s="XYZ"
# print(s.isdigit()) # False
#
# s="12.3"
# print(s.isdigit()) # False

# isnumeric(): returns True if all characters are numeric (0-9) else False,
# "-1" and "1.5" are NOT considered as numeric, as all characters in the string must be numeric
#  and the - and the . are not
# s="123"
# print(s.isnumeric()) # True
#
# s="XYZ"
# print(s.isnumeric()) # False
#
# s="12.3"
# print(s.isnumeric()) # False

# islower()
# isupper()

# s="welcome"
#
# print(s.islower()) # True
# print(s.isupper()) # False

t = "Python is a programming language and python is easy"
edit = t.replace("python is", "",1)
print(edit)
