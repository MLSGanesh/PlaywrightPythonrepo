# 1. Given [2, 7, 2, 4, 7, 9, 4], print the elements that appear exactly twice.

# n = [2, 7, 2, 4, 7, 9, 4]
# f = []
# g = []
# n = sorted(n)
# print(n)
# for i in range(len(n)):
#     for j in range(i+1,len(n)):
#         # for k in range(j+1,len(n)):
#             if n[i] == n[j]:
#                 f.append(n[i])
#             # elif n[j] != n[k]:
#             #     g.append(n[j])
# print(f)
#
# # correct one
# n = [2, 7, 2, 4, 7, 9, 4]
# d = set()
# for i in n:
#     if n.count(i)==2:
#      d.add(i)
# print(d)

# # 2. Get a string and check whether it contains only digits.
# a = str(input())
# d = []
# s = ""
# for c in a:
#     if c.isdigit():
#         d.append(c)
#     else:
#         s = c+s
# if s=="":
#     print("It contains only digits")
# else:
#     print("It doesn't contains only digits")

# # By Chat GPT
# a = str(input())
#
# if a.isdigit():
#     print("It contains only digits")
# else:
#     print("It doesn't contains only digits")

# # 3. Given [10, 15, 20, 25, 30], replace every element divisible by 10 with "X".
#
# n = [10, 15, 20, 25, 30]
# for i in range(len(n)):
#     if n[i] % 10 == 0:
#         n[i] = "X"
# print(n)

# # given by Chat GPT
# numbers = [10, 15, 20, 25, 30]
#
# for i in range(len(numbers)):
#     if numbers[i] % 10 == 0:
#         numbers[i] = "X"
#
# print(numbers)
# # Output: ['X', 15, 'X', 25, 'X']

# # 4. Given a dictionary of students and their subjects, create a list of students who study "Python".
#
# students = {
#     "Ravi": "Java",
#     "Anu": "Python",
#     "Kiran": "Python",
#     "Meena": "Testing"
# }
# l = []
# for key, value in students.items():
#     if value == "Python":
#         l.append(key)
# print(l)

# By Chat GPT

# students = {
#     "Ravi": "Java",
#     "Anu": "Python",
#     "Kiran": "Python",
#     "Meena": "Testing"
# }
#
# python_students = []
#
# for name, subject in students.items():
#     if subject == "Python":
#         python_students.append(name)
#
# print(python_students)
# # Output: ['Anu', 'Kiran']

# 5. Given "I am learning Python", reverse the order of words to get "Python learning am I".
# a = "I am learning Python"
# a = a.split()
# l = []
# n = 0
# for i in range(len(a)):
#     l.insert(n,a[i])
# l = " ".join(l)
# print(l)

# # by Chat GPT
# a = "I am learning Python"
# b = a.split()
# b.reverse()
# c = " ".join(b)
# print(c)

# # 1. Given [4, 8, 15, 16, 23, 42], print the difference between every adjacent pair.
# # Expected: [4, 7, 1, 7, 19]
#
# a = [4, 8, 15, 16, 23, 42]
# n = []
#
# for i in range(0,len(a)):
#     for j in range(i+1,len(a)):
#         n.append(a[j]-a[i])
#         break
# print(n)

# by Chat GPT
# numbers = [4, 8, 15, 16, 23, 42]
#
# differences = []
#
# for i in range(1, len(numbers)):
#     difference = numbers[i] - numbers[i - 1]
#     differences.append(difference)
#
# print(differences)
# # Output: [4, 7, 1, 7, 19]

# 2. Get a string and count how many characters are repeated more than once.
# a = "selenium python postman swagger"
# f = {}
# for c in a:
#     if c in f:
#         f[c] += 1
#     else:
#         f[c] = 1
# print(f)
# for key,value in f.items():
#     if value > 1:
#         print(key, ":", value)
#
# # by Chat GPT
# text = input("Enter a string: ")
#
# count = 0
# checked = []
#
# for char in text:
#     if text.count(char) > 1 and char not in checked:
#         count += 1
#         checked.append(char)
#
# print("Repeated characters count:", count)

# # 3. Given [1, 2, 3, 4, 5, 6, 7], remove all odd numbers without creating a new list.
#
# n = [1, 2, 3, 4, 5, 6, 7]
# for i in n:
#     if i%2  != 0:
#         n.remove(i)
# print(n)

# # by Chat GPT
# numbers = [1, 2, 3, 4, 5, 6, 7]
# numbers[:] = [n for n in numbers if n % 2 == 0]
# print(numbers)

# # 4. Given a dictionary of item names and prices, increase every price by 10%.
#
# prices = {"Pen": 10, "Book": 50, "Bag": 500}
# for key,value in prices.items():
#     value = (value*110)//100
#     prices[key] = value
#
# print(prices)
#
# # By Chat GPT
# prices = {"Pen": 10, "Book": 50, "Bag": 500}
# for value in prices:
#     prices[value] *= 1.10
# print(prices)

# # 5. Given "madam is level", print only the palindrome words.
# a = "madam is level"
# b = a.split()
# for c in b:
#     if c == c[::-1]:
#         print(c)
#
# # By Chat GPT
# text = "madam is level"
#
# for word in text.split():
#     if word == word[::-1]:
#         print(word)

# # 1. Given [3, 6, 9, 12, 15], check whether the list forms an arithmetic sequence.
# n = [3, 6, 9, 12, 15]
# d = 0
# for i in range(len(n)):
#     for j in range(i+1,len(n)):
#         for k in range(j+1,len(n)):
#             d = n[j]-n[i]
#             if d == (n[k]-n[j]):
#                 break
# print("It is an Arithmetic sequence")
#
# # By Chat GPT
# numbers = [3, 6, 9, 12, 15]
#
# difference = numbers[1] - numbers[0]
# is_arithmetic = True
#
# for i in range(2, len(numbers)):
#     if numbers[i] - numbers[i - 1] != difference:
#         is_arithmetic = False
#         break
#
# if is_arithmetic:
#     print("Arithmetic sequence")
# else:
#     print("Not an arithmetic sequence")

# # 2. Get a string and print the last non-repeated character.
# a = str(input())
# l = []
# s = {}
# for c in a:
#     if c in s and c not in l:
#         l.append(c)
#     else:
#         s[c] = 1
# print(s)
# print(s[-1])
#
# # Correct one
# text = input()
# l = "None"
# for c in text:
#     if text.count(c) == 1:
#         l = c
# if l is not None:
#     print("Last non repeated char:",l)
# else:
#     print("No non repeated char found")

# # 3. Given [1, 2, 3, 4, 5], create a new list containing the cumulative sum.
# # Expected: [1, 3, 6, 10, 15]
# n = [1, 2, 3, 4, 5]
# d = []
# s = 0
#
# for i in range(len(n)):
#     d.append(n[i]+s)
#     s = n[i]
# print(d)
#
# # Correct one
# n = [1, 2, 3, 4, 5]
# d = []
# s = 0
# for a in n:
#     s += a
#     d.append(s)
# print(d)

# # 4. Given a dictionary of students and marks, add 5 bonus marks only to students scoring below 50.
# students = {"Ravi": 45, "Anu": 78, "Kiran": 38, "Meena": 90}
# for key,value in students.items():
#     if value <= 50:
#         students[key] = value + 5
# print(students)
#
# # By Chat GPT
# students = {
#     "Ravi": 45,
#     "Anu": 78,
#     "Kiran": 38,
#     "Meena": 90
# }
#
# for name, marks in students.items():
#     if marks < 50:
#         students[name] = marks + 5
#
# print(students)

# # 5. Given "aabccdeff", print the characters that occur exactly once.
# a = "aabccdeff"
# for c in a:
#     if a.count(c) == 1:
#         print(c)
#
# # By Chat GPT
# text = "aabccdeff"
#
# for char in text:
#     if text.count(char) == 1:
#         print(char)