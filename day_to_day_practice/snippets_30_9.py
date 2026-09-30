# # 1. Given [10, 20, 30, 40, 50], swap the first and last elements.
#
# a = [10, 20, 30, 40, 50]
# a[0], a[-1] = a[-1],a[0]
# print(a)

# # 2. Given "selenium playwright pytest", print the word with the most characters.
#
# a = "selenium playwright pytest"
# a = a.split()
# l = ""
# for c in a:
#     if len(c) > len(l):
#         l = c
# print(l)

# # 3. Get a number and calculate the sum of all even digits in it.
# # Example: 123456 → 2 + 4 + 6 = 12.
#
# a = 456782
# a = abs(a)
# s = 0
# while a > 0:
#     d = a%10
#     if d%2 == 0:
#         s += d
#     a = a//10
# print(s)

# # 4. Given a dictionary of students and marks, create a new dictionary containing only students who passed (marks >= 40).
#
# students = {"Ravi": 35, "Anu": 78, "Kiran": 40, "Meena": 28}
# new = {}
# for key,value in students.items():
#     if value >= 40:
#         new[key] = value
# print(new)

# # 5. Given [1, 2, 3, 2, 4, 1, 5], remove all elements that occur more than once.
# # Expected output: [3, 4, 5]
#
# l = [1, 2, 3, 2, 4, 1, 5]
# s = []
#
# for c in l:
#     if l.count(c) == 1:
#         s.append(c)
# print(s)

# # 1. Given [7, 2, 9, 4, 6], find the sum of the two largest distinct numbers.

# n = [7, 2, 9, 4, 6]
# l = 0
# s = 0
# for c in n:
#     if c > l:
#         s=l
#         l=c
#     elif s>c and c != l:
#         s = c
# print(l+s)

# # 2. Get a string and print the first vowel in it. If no vowel exists, print "No vowel found".
#
# a = str(input())
# v = ["a","e","i","o","u","A","E","I","O","U"]
# for c in a:
#     if c in v:
#         print(c)
#         break
# else:
#         print("No vowel found")

# # 3. Given [1, 2, 3, 4, 5, 6], reverse only the even numbers while keeping odd numbers in their original positions.
# # Expected output: [1, 6, 3, 4, 5, 2]
#
# n = [1, 2, 3, 4, 5, 6]
# e = []
# for c in n:
#     if c%2 == 0:
#         e.append(c)
# e.reverse()
# index = 0
# for i in range(len(n)):
#     if n[i] %2 ==0:
#         n[i]=e[index]
#         index += 1
# print(n)

# # 4. Given a dictionary of student names and marks, print the student with the second-highest distinct mark.
#
# students = {"Ravi": 85, "Anu": 92, "Kiran": 85, "Meena": 78}
# u = []
#
# for m in students.values():
#     if m not in u:
#         u.append(m)
#
# u.sort(reverse=True)
# s = u[1]
# for name,mark in students.items():
#     if mark == s:
#         print(name,":", mark)

# # 5. Given "Python is fun and Python is powerful", print each word with its frequency, ignoring uppercase/lowercase differences.
# a = 'Python is fun and Python is powerful'
# a = a.lower()
# a = a.split()
# f = {}
# for c in a:
#     if c in f:
#         f[c] += 1
#     else:
#         f[c] = 1
# print(f)

# # 1. Given [8, 3, 5, 3, 9, 8, 1], find the element with the second-highest frequency.
#
# n = [8, 3, 5, 3, 9, 8, 1]
# d = {}
#
# for c in n:
#     if c in d:
#         d[c] += 1
#     else:
#         d[c] = 1
# print(d)
# a = list(set(d.values()))
# a.sort(reverse=True)
# s = a[1]
# for key,value in d.items():
#     if value == s:
#         print(key, value)

# # 2. Get a sentence and print all words that contain the letter "a".
#
# s = "guava have great benefits for health"
# s = s.split()
# for c in s:
#     if "a" in c.lower():
#         print(c)

# # 3. Given [10, 20, 30, 40, 50], insert 25 after 20.
#
# n = [10, 20, 30, 40, 50]
# i  = n.index(20)
# n.insert(i+1,25)
# print(n)

# # 4. Given a dictionary of employee names and departments, count how many employees belong to each department.
#
# employees = {
#     "Ravi": "QA",
#     "Anu": "Development",
#     "Kiran": "QA",
#     "Meena": "HR",
#     "Priya": "Development"
# }
# f = {}
# for value in employees.values():
#     if value in f:
#         f[value] += 1
#     else:
#         f[value] = 1
# print(f)

# # 5. Get a number and check whether it is a Harshad number.
# # A Harshad number is divisible by the sum of its digits. Example: 18 ÷ (1 + 8) = 2.
#
# number = int(input("Enter a number: "))
#
# original_number = number
# sum_of_digits = 0
#
# while number > 0:
#     digit = number % 10
#     sum_of_digits += digit
#     number = number // 10
#
# if original_number % sum_of_digits == 0:
#     print("Harshad number")
# else:
#     print("Not a Harshad number")

# # input = "python is a programming language and python is easy"
# # output = "python is a programming language and easy"
#
# input = "python is a programming language and python is easy"
# words = input.split()
# l = []
# for c in words:
#     if c not in l:
#         l.append(c)
# print(l)
# l = " ".join(l)
# print(l)