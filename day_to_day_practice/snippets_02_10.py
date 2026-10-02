# 1. Given [5, 1, 5, 2, 3, 2, 4], print the elements that occur more than once, along with their counts.
# n = [5, 1, 5, 2, 3, 2, 4]
# f = {}
# for i in n:
#     if i > 1 and i in f:
#         f[i] += 1
#     else:
#         f[i] = 1
# print(f)
# g = {}
# for key,value in f.items():
#     if value > 1:
#         g[key] = value
# print(g)
#
# # By Chat GPT
# numbers = [5, 1, 5, 2, 3, 2, 4]
#
# frequency = {}
#
# for number in numbers:
#     if number in frequency:
#         frequency[number] += 1
#     else:
#         frequency[number] = 1
#
# for number, count in frequency.items():
#     if count > 1:
#         print(number, "appears", count, "times")

# # 2. Get a string and replace every vowel with *.
# a = input()
# v = "aeiou"
# for c in a:
#     if c in v:
#         c = "*"
# print(a)
#
# # Correct one
# a = input()
# r = ""
# for c in a:
#     if c.lower() in "aeiou":
#         r += "*"
#     else:
#         r += c
# print(r)

# # 3. Given [1, 2, 3, 4, 5, 6], find the sum of elements at odd indexes.
# n = [1, 2, 3, 4, 5, 6]
# s = 0
# for i in range(len(n)):
#     if i%2 != 0:
#         s += n[i]
# print(s)
#
# # By Chat GPT
# numbers = [1, 2, 3, 4, 5, 6]
#
# total = 0
#
# for i in range(len(numbers)):
#     if i % 2 != 0:
#         total += numbers[i]
#
# print("Sum:", total)
# # Output: 12

# # 4. Given a dictionary of products and stock, print the products that are out of stock (stock = 0).
#
# stock = {"Pen": 10, "Book": 0, "Bag": 5, "Pencil": 0}
#
# for key, value in stock.items():
#     if value == 0:
#         print(key)
#
# # By Chat GPT
# stock = {
#     "Pen": 10,
#     "Book": 0,
#     "Bag": 5,
#     "Pencil": 0
# }
#
# for product, quantity in stock.items():
#     if quantity == 0:
#         print(product)

# # 5. Given "abcabcbb", find the length of the longest substring without repeating characters.
# a = "abcabcbb"
# r = ""
# for c in a:
#     if c not in r:
#         r += c
# print(len(r))
#
# # Correct One
# a = "abcabcbb"
# r = ""
# l = 0
# for c in a:
#     if c in r:
#         i = r.index(c)
#         r = r[i+1:]
#     r += c
#     if len(r) > l:
#         l = len(r)
# print(l)

# # 1. Given [10, 20, 10, 30, 20, 40], create a dictionary showing the frequency of each number.
# n = [10, 20, 10, 30, 20, 40]
# f = {}
# for i in n:
#     if i in f:
#         f[i] += 1
#     else:
#         f[i] = 1
# print(f)
#
# #  By Chat GPT
# numbers = [10, 20, 10, 30, 20, 40]
#
# frequency = {}
#
# for number in numbers:
#     if number in frequency:
#         frequency[number] += 1
#     else:
#         frequency[number] = 1
#
# print(frequency)

# # 2. Get a string and print the number of uppercase and lowercase vowels separately.
# # a = str(input())
# a = "dElhi"
# v = "aeiou"
# u = 0
# l = 0
# for c in a:
#     if c in v:
#         l += 1
#     elif c in v.upper():
#         u += 1
# print("Upper Case:",u)
# print("Lower Case:",l)
#
# # By Chat GPT
# text = input("Enter a string: ")
#
# uppercase_vowels = 0
# lowercase_vowels = 0
#
# for char in text:
#     if char in "AEIOU":
#         uppercase_vowels += 1
#     elif char in "aeiou":
#         lowercase_vowels += 1
#
# print("Uppercase vowels:", uppercase_vowels)
# print("Lowercase vowels:", lowercase_vowels)

# # 3. Given [5, 2, 8, 1, 9], swap the smallest and largest elements.
# n = [5, 2, 8, 1, 9]
# l = max(n)
# s = min(n)
# print(l)
# print(s)
# for i in range(len(n)):
#     if n[i] == l:
#         n.remove(n[i])
#         n.insert(i,l)
#     if n[i] == s:
#         n.remove(n[i])
#         n.insert(i, s)
# print(n)
#
# #  Correct one
# n = [5, 2, 8, 1, 9]
# l = 0
# s = 0
# for i in range(1,len(n)):
#     if n[i] < n[s]:
#         s = i
#     if n[i] > n[l]:
#         l = i
# n[s] , n[l] = (n[l],n[s])
# print(n)

# # 4. Given a dictionary of students and attendance percentages, print students whose attendance is below 75.
# attendance = {"Ravi": 82, "Anu": 70, "Kiran": 95, "Meena": 68}
# for key, value in attendance.items():
#     if value < 75:
#         print(key)
#
# # By Chat GPT
# attendance = {
#     "Ravi": 82,
#     "Anu": 70,
#     "Kiran": 95,
#     "Meena": 68
# }
#
# for student, percentage in attendance.items():
#     if percentage < 75:
#         print(student, ":", percentage)

# # 5. Given "Python is easy and powerful", find the total number of characters excluding spaces.
# a = "Python is easy and powerful"
# T = 0
# for c in a:
#     if c != " ":
#         T += 1
# print(T)
#
# # Chat GPT
# text = "Python is easy and powerful"
#
# count = 0
#
# for char in text:
#     if char != " ":
#         count += 1
#
# print("Characters excluding spaces:", count)
# # Output: 22

