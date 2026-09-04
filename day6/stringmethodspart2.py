# isdecimal()
# isdigit()
# isnumeric()
# These are string related methods where numbers are stored as string, and won't work for int

# isdecimal()

# Returns True if all characters in the string are decimal characters (0–9 only).
# These are strictly digits used to form base-10 numbers.
#Base-10 numbers, also known as decimal numbers, use the digits 0 through 9 to represent any number.
# It's the number system we commonly use.
# Does not consider superscripts, fractions, or Roman numerals as valid decimals.

# print("123".isdecimal()) # True
# print("①②③#$".isdecimal()) # False
# print("12.3".isdecimal()) # False

# isdigit()
# Returns True if all characters are digits.
# Digits include decimal digits (0–9)
# Allows other digit characters, such as superscripts, subscript digits, or digits from other numeral systems.
# Does not consider superscripts, fractions, or Roman numerals as valid decimals.

# print("123".isdigit()) # True
# print("²³".isdigit()) #True
# print("①②③".isdigit()) # True
# print("12.3".isdigit()) # False (.(dot) doesn't come under decimal number system)

#isnumeric()
# Returns True if all characters are numeric.
# This is the broadest check — includes digits, decimals, Roman numerals, currency numerators, etc.
# Accepts everything isdecimal() and isdigit() accept, plus additional numeric characters.

# print("123".isnumeric())  #True
# print("²³".isnumeric()) #True
# print("①".isnumeric()) #True
# print("⅔".isnumeric())  #True
# print("10.5".isnumeric()) #False

# split(): splitting strings
# split is based on delimmiter, examples of delimmiters are space( ),@,comma(,), #, &, _, :, ;, ()

# Example 1:
# s='abc@gmail.com'
# lst=s.split("@")
# print(type(lst)) #list
# print(lst) # ['abc', 'gmail.com']
# print(lst[0]) # abc
# print(lst[1]) # gmail.com

# Example 2:
# s="one,two,three"
# lst= s.split(",")
# print(lst)
# print(lst[2])

# startswith() - returns True/False

# s="welcome"
# print(s.startswith("wel")) # True
# print(s.startswith("Wel")) # False

# endswith() - returns True/False

# s="hello.py"
# print(s.endswith("py")) # True
# s="welcome"
# print(s.endswith("me")) # True

# Trimming spaces -> strip(), lstrip(), rstrip()

s=" hello "
print(s.strip())
print(s.lstrip())
print(s.rstrip())


