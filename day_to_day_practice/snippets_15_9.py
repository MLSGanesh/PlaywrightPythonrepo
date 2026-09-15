# # 1. Given [10, 20, 30, 40, 50], find the average without using sum().
#
# a = [10, 20, 30, 40, 50]
# b = len(a)
# d = 0
# print(b)
# for c in a:
#     d = d + c
#     # print(d)
# print(d//b)

# # 2. Get a string and remove all vowels from it.
# a = str(input()).lower()
# b = 'aeiou'
# d = ""
# for i in a:
#     if i not in b:
#         d += i
# print(d)

# # 3. Given [1, 2, 3, 4, 5], find the product of all elements.
#
# a = [1, 2, 3, 4, 5]
# b = 1
# for c in a:
#     b = b*c
# print(b)

# # 4. Get a number and check whether it is a strong number. Example: 145 = 1! + 4! + 5!.
#
# n = int(input())
# o = n
# s = 0
#
# while n > 0:
#     d = n%10
#
#     f = 1
#     for i in range(1,d+1):
#         f *= i
#
#     s += f
#     n = n//10
#
# if s==o:
#     print("This is a Strong Number")
# else:
#     print("This is not a Strong Number")

# # 5. Given "banana", print the character with the highest frequency.
# f = "banana"
# b = ""
# d = 0
#
# for i in f:
#     c = f.count(i)
#
#     if c > d:
#         d = c
#         b = i
# print(d)
# print(b)

# # 6. Given [1, 3, 5, 7], insert 4 in the correct position to keep the list sorted.
#
# a = [1, 3, 5, 7]
# l = len(a)
# b = 4
# for i in range(l):
#     if a[i] > b:
#         a.insert(i,b)
#         break
# print(a)

# # 7. Given [1, 2, 3, 4, 5], print all pairs whose sum is 6.
#
# a = [1, 2, 3, 4, 5]
# b = 6
# for c in range(len(a)):
#     for d in range(c+1,len(a)):
#         if a[c] + a[d] == b:
#             print(a[c], a[d])

# # 8. Given two dictionaries, merge them into one dictionary.
#
# d1 = {"Brand":"Ford","Model":'Aspire',"Year":2024, "Color":"Red"}
# d2 = {"Team":"AUS","Format":'Test',"Matches":15, "Won":10}
# d = {}
#
# for key, value in d1.items():
#     d[key] = value
#
# for key, value in d2.items():
#     d[key] = value
# print(d)

# # 9. Get a sentence and print the longest word.
#
# a = "python is a programming language and python is easy"
# b = a.split()
# c = ""
# for i in b:
#     if len(i) > len(c):
#         c = i
# print(c)

# # 10. Given a list of numbers, move all zeroes to the end while keeping the order of non-zero elements. numbers = [0, 1, 0, 3, 12]
#
# n = [0, 1, 0, 3, 12]
# l = []
# c = 0
# for i in n:
#     if i != c:
#         l.append(i)
# for i in n:
#     if i == c:
#         l.append(i)
# print(l)

# # 11. Given "abc123xyz45", calculate the sum of all digits.
#
# a = "abc123xyz45"
# c = 0
# for i in a:
#     if i.isnumeric(): # can use isdigit also
#         c += int(i)
# print(c)

# # 12. Given nested lists, flatten them into one list. numbers = [[1, 2], [3, 4], [5, 6]]
# # Expected: [1, 2, 3, 4, 5, 6]
#
# numbers = [[1, 2], [3, 4], [5, 6]]
# a = []
# for i in numbers:
#     for j in i:
#         a.append(j)
# print(a)