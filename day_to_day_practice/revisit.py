# # 1. Reverse a String
# a = "String"
# b = a[::-1]
# print(b)

# a = "String"
# r = ""
# for c in a:
#     r = c+r
# print(r)

# # 2.Check for palindrome
# a = str(input())
# b = a[::-1]
# if a==b:
#     print("It is a Palindrome")
# else:
#     print("It is not a Palindrome")

# # 3. Fibonacci Series
# def fib(n):
#     b,c = 0,1
#     for _ in range(n):
#         print(b)
#         b,c = c,b+c
# print(fib(10))

# # 4. Check for prime number
# n = int(input())
#
# if n < 2:
#     print("Not a Prime Number")
# else:
#     is_prime = True
#
#     for i in range(2,n):
#         if n%i == 0:
#             is_prime = False
#             break
#     if is_prime==True:
#         print("It is a Prime Number")
#     else:
#         print("Not a Prime Number")

# # 5. Factorial
# a = int(input())
# b = 1
# for i in range(1, a+1):
#     b = b*i
# print(b)

# # 6. Find duplicate characters and elements
# a = "automation"
# s = set()
# d = []
# for i in a:
#     if i in s and i not in d:
#         d.append(i)
#     else:
#         s.add(i)
# print(s)
# print(d)

# n = [1,2,2,4,5,3,6,4]
# s = set()
# d = []
# for i in n:
#     if i in s and i not in d:
#         d.append(i)
#     else:
#         s.add(i)
# print(s)
# print(d)

# # 7. Remove Duplicates
#
# a = "automation"
# s = set()
# d = []
# for i in a:
#     if i in s and i not in d:
#         d.append(i)
#     else:
#         s.add(i)
# print(s)

# n = [1,2,2,4,5,3,6,4]
# s = set()
# d = []
# for i in n:
#     if i in s and i not in d:
#         d.append(i)
#     else:
#         s.add(i)
# print(s)

# # 8. Find largest and second largest element
#
# a = [99,2,1,6,45,210,122,12]
# b = list(set(a))
# b.sort(reverse=True)
# print(b)
# print(b[0])
# print(b[1])

# # 9. Sort an Array
# a = [99,2,1,6,45,210,122,12]
# a.sort()
# print(a)
#
# b = ["Car", "Keys","Start","Accelerate"]
# b.sort()
# print(b)

# # 10. Find the missing number
#
# n = [1,2,4,5,6]
# b = next(i for i in range(min(n),max(n)+1) if i not in n)
#  or
# for i in range(min(n),max(n)+1):
#     if i not in n:
#         print(i)

# # 11. Check for Anagram
# a = str(input())
# b = str(input())
# if sorted(a) == sorted(b):
#     print("It is an Anagram")
# else:
#     print("Not an Anagram")

# # 12. character frequency
#
# a = "automation"
# f = {}
# for i in a:
#     if i in f:
#         f[i]+=1
#     else:
#         f[i]=1
# print(f)

# # 14. Find the first non-repeated character
#
# def rep(a):
#     for c in a:
#         if a.count(c)==1:
#             return c
#     return None
# a = "aaabbbcbddeb"
# print(rep(a))

# 15. Merge two Arrays
# a = [1,2,3,4,5,6]
# b = [3,2,34,65,4]
# s = a+b
# print(s)
#
# a = ["a","b",'v','ball']
# b = ['new','array']
# s = a+b
# print(s)

# 16. Find common elements
# a = str(input())
# b = str(input())
# s = set()
# for c in a:
#     if c in a and c in b:
#         s.add(c)
# print(s)

# a = [1,2,3,5,8,2]
# b = [3,2,4,7,9]
# s = set()
# for c in a:
#     if c in a and c in b:
#         s.add(c)
# print(s)