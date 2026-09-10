from collections import Counter

# reverse a string

# a = "satya"
# b = a[::-1]
# print(b)

# reverse without using [::-1]

# def reverse_s(text):
#     r = ""
#     for c in text:
#         r=c+r
#     return r
# print(reverse_s("satya"))


# find duplicate elements in a list

# a = [1,2,1,3,4,3,5]
# s=set()
# d=[]
# for n in a:
#     if n in s and n not in d:
#         d.append(n)
#     else:
#         s.add(n)
#
# print(d)

# find second largest number

# a = [1,2,10,2,100,32]
# print(len(a))
# b = list(set(a))
# b.sort(reverse=True)
# print(b[1])

# count character frequency

# a = str(input())
# f={}
# for c in a:
#     if c in f:
#         f[c]+=1
#     else:
#         f[c]=1
# print(f)

# # using counter collection
# text=str(input())
# count = Counter(text)
# print(count)


# find missing number

# a = [1,2,4,5,6]
# m = next(n for n in range(min(a),max(a)+1) if n not in a)
# print(m)

# a = [1,2,4,5,6]
#
# for n in range(min(a),max(a)+1):
#     if n not in a:
#         print(n)

# compare two lists

# a = ["apple", "banana","avacado","eagle"]
# b = ["cherry", "apple","eagle"]
#
# x=[]
# y=[]
#
# for i in a:
#     if i not in b:
#         x.append(i)
# for i in b:
#     if i not in a:
#         y.append(i)
#
# print(x)
# print(y)

# Extract names from JSON

# response = {
#     "users": [
#         {"id": 1, "name": "John"},
#         {"id": 2, "name": "David"},
#         {"id": 3, "name": "Smith"}
#     ]
# }
#
# names = [user.get("name")
#          for user in response.get("users", [])]
# print(names)

#
#
# l = [1,2,3,5,8,12,100,32,1123]
#
# l = list(x for x in l if x != 2)
#
# s=l.sort(reverse=True)
# # print(sorted(l))
# # l.reverse()
# # print(len(l))
# # l.reverse()
# print(s)
#
# # l.insert(3,4)
# # print(l)
#
# # s=[]
# # for n in l:
# #     s.append(n**2)
# #
# # print(s)
#
# # for n in range(len(l)):
# #     l[n]=l[n]**2
# #
# # print(l)
#
# # l=[i**2 for i in l ]
# #
# # print("New",l)
#
# # s = list(map(lambda i: i**2,l))
# # print(s)

# factorial

# n=int(input())
# f=1
#
# for i in range(1,n+1):
#     f=f*i
# print(f)

# find duplicates

# a = "automation"
# s=set()
# d=[]
# for c in a:
#     if c in s and c not in d:
#         d.append(c)
#     else:
#         s.add(c)
#
# print(d)

# find maximum and second largest number

# l = [1,2,3,5,8,12,100,2,32,1123]
# print(max(l))
# l.sort()
# l.reverse()
# print(l)
# s = list(set(l))
# s.sort(reverse=True)
# print(s[1])

# find missing number

# l = [1,2,3,5,8,12]
# m=list(n for n in range(min(l), max(l)+1) if n not in l)
# print(m)

# update the sentence

# # input = "python is a programming language and python is easy"
# # output = "python is a programming language and easy"
#
# input = "Hi Lokesh How are you Lokesh what are you doing"
#
# words = input.split()
# list = []
# for c in words:
#     if c not in list:
#         list.append(c)
# output = " ".join(list)
# print(output)

# even number

# n = int(input())
# if n%2==0:
#     print("Even Number")
# else:
#     print("Not an even number")

# print second highest score

# score = [2,3,66,97,88,88,100,101]
#
# a = list(set(score))
# a.sort(reverse=True)
# print(a)
# print(a[1])

# caseswap

# a= "Hello World"
# # b=a.swapcase()
# # print(b)
# b = []
#
# for c in a:
#     if c == c.upper():
#         b.append(c.lower())
#     else:
#         b.append(c."upper"())
#
# b = "".join(b)
# print(b)
# # using list comprehension
# s = "".join([ c.lower() if c.isupper() else c.upper() for c in a])
# print(s)

# # print lowest score persons
# records = [["alpha",120.0],["beta",50.0],["theta",55.0],["dootha",60.0]]
#
# # for c in records:
# #     for a in c:
# #         if c[a][1]
#
# # s = min(record[1] for record in records)
# #
# # for name, score in records:
# #     if score == s:
# #         print(name)
#
# s = list(record[1] for record in records)
# s.sort(reverse=True)
# print(s)
# for name, score in records:
#     if score == s[1]:
#         print(name)


