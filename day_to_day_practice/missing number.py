import math

# string reverse


# a="Lokesh"
# b = a[::-1]
# print(b)

# palindrome

# a=input()
# b=a[::-1]
# if a==b:
#     print("It is a Palindrome")
# else:
#     print("It is not a Palindrome")

# fibnocci series

# def fib(n):
#     a,b=0,1
#     for _ in range(n):
#         print (a)
#         a,b = b,a+b
#
# print(fib(10))

# prime numbers

# number = int(input("Enter a number: "))
#
# if number < 2:
#     print("Not a prime number")
# else:
#     is_prime = True
#
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#             break
#
#     if is_prime:
#         print("Prime number")
#     else:
#         print("Not a prime number")

# factorial

# n = int(input())
# f = 1
# for i in range(1, n+1):
#     f=f*i
# print("Factorial: ", f)

# find duplicate chars/elements

# t="automation"
#
# seen =set()
# duplicates=[]
#
# for c in t:
#     if c in seen and c not in duplicates:
#         duplicates.append(c)
#     else:
#         seen.add(c)
# print(seen)
# print(duplicates)

# n = [1,2,3,4,5,3,5,2,6,10,11,12]
#
# seen = set()
# duplicates = []
#
# for c in n:
#     if c in seen and c not in duplicates:
#         duplicates.append(c)
#     else:
#         seen.add(c)
# print(seen)
# print(duplicates)

# remove duplicates

# t="automation"
#
# s=set()
# d = []
# for c in t:
#     if c in s and c not in d:
#         d.append(c)
#     else:
#         s.add(c)
# print(s)


# n = [1,1,2,2,3,4,5,5]
#
# s= set()
# d=[]
# for c in n:
#     if c in s and c not in d:
#         d.append(c)
#     else:
#         s.add(c)
# print(s)


# find maximum and second largest element

# n = [10,4,100,1,2,5,1112,1]
# print(max(n)) # to find max number
# print(len(n))  # just to verify list count
# l = list(set(n))
# l.sort(reverse=True)
# print(l[0])
# print(l[1])
# print(len(l)) # just to confirm final set count

# sort an array
# n = [10,4,100,1,2,5,1112,1]
# n.sort()
# print(n)
#
# a= ["fruit","cherry","apple"]
# a.sort()
# print(a)

# find missing number

# a = [1, 2, 4, 5]
#
# m = next(n for n in range(min(a), max(a) + 1) if n not in a)
#
# print(m)  # 4

# a = [1, 2, 4, 5]
#
# print(min(a))
# print(max(a))

# check for anagram

# a=str(input())
# b=str(input())
#
# # for c in a:     # my own thinking
# #     if c in a and c in b:
# #         print("it is an Anagram")
# #     else:
# #         print("it is not an Anagram")
#
# if sorted(a) == sorted(b):
#     print("It is an Anagram")
# else:
#     print("It is not an Anagram")

# character frequency

# a=str(input())
#
# f={}
#
# for c in a:
#     if c in f:
#         f[c]+=1
#     else:
#         f[c]=1
# print(f)