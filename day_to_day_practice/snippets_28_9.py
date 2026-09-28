# # 1.	Given [3, 1, 4, 1, 5, 9, 2], find the first repeated element.
#
# a = [3, 1, 4, 1, 5, 3, 9, 2]
# b = set()
# d = None
# for c in a:
#     if c in b:
#         d = c
#         break
#     b.add(c)
# print(d)

# # 2. Get a sentence and print the shortest word.
#
# s = "python is programming language and python is easy"
# # a = set(s.split())
# a = s.split()
# print(a)
# x = a[0]
# print(x)
# for c in a:
#     if len(c) < len(x):
#         x = c
# print(x)

# # 3. Given "Hello123World456", extract all digits and form the number 123456.
#
# a = "Hello123World456"
# d = ""
# for c in a:
#     if c.isdigit():
#         d += c
# print(d)

# # 4. Given a list of numbers, count how many are positive, negative, and zero.
#
# numbers = [4, -2, 0, 7, -5, 0, 3]
# p = 0
# n = 0
# z = 0
# for number in numbers:
#     if number > 0:
#         p += 1
#     elif number < 0:
#         n += 1
#     else:
#         z += 1
#
# print("Positive: ", p)
# print("Negative: ", n)
# print("Zeros: ", z)

# # 5. Given two dictionaries, find the keys that exist in both dictionaries.
#
# d1 = {"Brand":"Ford","Model":'Aspire',"Country":"England","Year":2024,"Continent":"Europe", "Color":"Red"}
# d2 = {"Country":"AUS","Format":'Test',"Matches":15, "Won":10, "Continent":"Australia"}
# # d3 = {} # for fetching key and values
# d3 = []
# for key,value in d1.items():
#     if key in d2:
#         d3.append(key)
#         # d3[key] = value
# print(d3)

# # 1. Given [10, 15, 20, 25, 30], create a list containing only numbers divisible by 10.
#
# a = [10, 15, 20, 25, 30]
# l = []
# for c in a:
#     if c%10 == 0:
#         l.append(c)
# print(l)

# # 2. Get a string and print the first character that appears more than once.
#
# a = "hi how are you"
# s = set()
# d = ""
# for c in a:
#     if c in s:
#         d = c
#         break
#     s.add(c)
# print(d)

# # 3. Given [1, 2, 3, 4, 5], calculate the sum of squares of all elements.
#
# a = [1, 2, 3, 4, 5]
# d = 0
# for c in a:
#     d += c**2
# print(d)

# # 4. Given a dictionary of products and prices, print the product with the highest price.
#
# products = {"Pen": 20, "Book": 100, "Bag": 500, "Pencil": 10}
# h = 0
# product = ""
# for key,value in products.items():
#     if value > h:
#         h = value
#         product = key
# print(product)
# print(h)

# 5. Given "Python is easy to learn", replace every space with a hyphen (-).
#
# a = "Python is easy to learn"
# s = " "
# for c in a:
#     if c == s:
#         a = a.replace(c,"-")
# print(a)

# # or
#
# a = "Python is easy to learn"
# a = a.replace(" ","-")
# print(a)

# # 1. Given [5, 10, 15, 20, 25], print the sum of elements at even indexes.
#
# a = [5, 10, 15, 20, 25]
# s = 0
# d = 0
# for c in range(0,len(a)):
#     if c%2 == 0:
#         d = a[c]
#         s += d
# print(s)

# # 2. Get a string and count how many times each vowel appears.
# a = "Hi how are you, whAt arE yOU dOIng"
# # a = a.split()
# # print(a)
# vowels = {"a":0,"e":0,"i":0,"o":0,"u":0,"A":0,"E":0,"I":0,"O":0,"U":0}
#
# for c in a:
#     if c in vowels:
#         vowels[c] += 1
# print(vowels)

# # 3. Given [2, 4, 6, 8, 10], check whether all elements are even.
# a = [2, 4, 6, 8, 10]
# b = []
# for c in a:
#     if c%2 == 0:
#         b.append(c)
# # sorted(a)
# # sorted(b)
# print(b)
# if a == b:
#     print("All are Even")
# else:
#     print("All are not even")

# # 4. Given a dictionary of employees and salaries, print the employees whose salary is greater than 50,000.
# employees = {"Ravi": 45000, "Anu": 60000, "Priya": 75000, "Kiran": 50000}
# emp = []
# for key,value in employees.items():
#     if value > 50000:
#         emp.append(key)
# print(emp)

# # 5. Given "programming", print all characters that occur only once.
#
# a = "programming"
#
# for c in a:
#     if a.count(c) == 1:
#         print(c)
