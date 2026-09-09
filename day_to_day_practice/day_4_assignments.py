# Get a number from the user and print whether it's positive, negative, or zero.

# n = int(input())
#
# if n > 0:
#     print("Positive")
# elif n < 0:
#     print("Negative")
# else:
#     print(n,": Zero")

# Take a single letter as input and check if it's a vowel (a, e, i, o, u) or a consonant.

# a = str(input()).lower
# vowels = ['a','e','i','o','u']
#
# for v in a:
#     if v in vowels:
#         print("it is a Vowel")
#     else:
#         print("It is a Consonant")

 # Get a student's score (0-100) and assign a letter grade (A, B, C, D, or F) based on a simple scale.

# score = int(input())
#
# if score >= 90 and score <=100:
#     print("A Grade")
# elif score >= 75 and score <90:
#     print("B Grade")
# elif score >= 55 and score <75:
#     print("C Grade")
# elif score >= 35 and score <55:
#     print("D Grade")
# elif score >= 0 and score <35:
#     print("Fail")
# else:
#     print("Invalid Score")

# Get a number and calculate the sum of its digits using a while loop.
# For example, for the number 123, the sum is 1+2+3=6.

# n = int(input())
# sum = 0
#
# while n > 0:
#     d = n % 10
#     sum += d
#     n //= 10
# print(sum)

#  Take a number and print its reverse. For example, reversing 1234 gives 4321.

# n = int(input())
# r = 0
# while n > 0:
#     d = n%10
#     r = r * 10+d
#     n //=10
# print(r)

# Print the multiplication table for a number entered by the user, up to 10.
# n = int(input())
#
# for i in range(1, 11):
#     print("{0} x {1} = {2}".format(n,i,n*i))