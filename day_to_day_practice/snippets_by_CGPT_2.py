# # 1.	Get a number and print all even numbers from 1 to that number.
#
# n = int(input())
# for a in range(1,n+1):
#     if a%2==0:
#         print(a)
from numpy.ma.core import append

# # 2.	Given [4, 7, 2, 9, 1], find the difference between the largest and smallest element.
#
# a = [4, 7, 2, 9, 1]
# b = list(set(a))
# b.sort()
# c = b[0]
# b.reverse()
# d = b[0]
# d = d-c
# print(d)

# # 3.	Get a string and count uppercase letters, lowercase letters, digits, and spaces.
# a = str(input())
# u = 0
# l = 0
# d = 0
# s = 0
#
# for c in a:
#     if c.isupper():
#         u += 1
#     elif c.islower():
#         l += 1
#     elif c.isdigit():
#         d += 1
#     elif c.isspace():
#     # else:
#         s += 1
#
# print("Uppercase: ",u)
# print("Lowercase: ",l)
# print("Digits: ",d)
# print("Spaces: ",s)

# # 4.	Given [1, 2, 3, 4, 5], create a new list with each number doubled.
#
# a = [1, 2, 3, 4, 5]
# b = []
# for c in a:
#     b.append(c*2)
# print(b)

# # 5.	Given "hello world", reverse each word individually to get "olleh dlrow".
#
# a = "hello world"
# # b = a[::-1]
# # print(b)
# b = a.split(" ")
# print(b)
# r = []
# for c in b:
#     r.append(c[::-1])
# f = " ".join(r)
# print(f)

# # 6.	Get a number and print whether it is a perfect number. Example: 6 = 1 + 2 + 3.
#
# a = int(input())
# s = 0
# for c in range(1,a):
#     if a % c == 0:
#         s += c
# if a > 0 and s == a:
#     print("It is a Perfect Number")
# else:
#     print("It is not a Perfect Number")

# # 7.	Given [1, 2, 3, 4, 5], rotate the list one position to the right: [5, 1, 2, 3, 4].
#
# a = [1, 2, 3, 4, 5]
# l = a[-1]
# # print(l)
# a.pop()  # will remove last element
# a.insert(0,l)
# print(a)

# # 8.	Given two strings, check whether one string is a rotation of the other. Example: "abcd" and "cdab".
#
# string1 = "abcd"
# string2 = "cdab"
#
# if len(string1) == len(string2) and string2 in (string1 + string1):
#     print("Strings are rotations of each other")
# else:
#     print("Strings are not rotations of each other")


# # 9.	Given [1, 2, 3, 4, 5, 6], split it into separate even and odd lists.
#
# a = [1, 2, 3, 4, 5, 6]
# b = []
# c = []
#
# for i in a:
#     if i%2 == 0:
#         b.append(i)
#     elif i%2 == 1:
#         c.append(i)
# print(b)
# print(c)

# # 10.	Given "I love Python and Python is easy", find the word that occurs most frequently.
#
# a = "I love Python and Python is easy"
# b = a.lower().split()
# f = {}
#
# for c in b:
#     if c in f:
#         f[c] += 1
#     else:
#         f[c] = 1
#
# m = ""
# h_c = 0
# for c,count in f.items():
#     if count > h_c:
#         m = c
#         h_c = count
#
# print(m)
# print(h_c)

# # 11.	Given a dictionary: student = {"name": "Lokesh", "marks": 85, "grade": "A"} Print each key and value using a loop.
#
# student = {"name": "Lokesh", "marks": 85, "grade": "A"}
#
# for key,value in student.items():
#     print(key, ":", value)

# # 12.	Get a number and print its reverse. Example: 1234 → 4321.
#
# a = int(input())
# b = str(a)
# b = b[::-1]
# print(a)
# print(b)

# or

# number = int(input("Enter a number: "))
#
# reverse = 0
#
# while number > 0:
#     digit = number % 10
#     reverse = reverse * 10 + digit
#     number = number // 10
#
# print("Reversed number:", reverse)