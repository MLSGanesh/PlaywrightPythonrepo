# # 1. Given [1, 2, 2, 3, 4, 4, 5], create a list containing only the unique elements that appear once.
# # Expected: [1, 3, 5]
# n = [1, 2, 2, 3, 4, 4, 5]
# s = set()
# d = []
# for i in n:
#     if i in s and i not in d:
#         d.append(i)
#     else:
#         s.add(i)
# r = list(s)
# m = []
# for j in r:
#     if j in r and j not in d:
#         m.append(j)
# print(m)
#
# # By Chat GPT
# n = [1, 2, 2, 3, 4, 4, 5]
# l = []
# for i in n:
#     if n.count(i) == 1:
#         l.append(i)
# print(l)

# # 2. Get a string and count how many times a given character occurs, ignoring case.
# a = str(input())
# b = a.lower()
# c = input().lower()
# if c in a:
#     print(a.count(c))
#
# # By Chat GPT
# text = input("Enter a string: ")
# character = input("Enter a character: ")
#
# count = 0
#
# for char in text:
#     if char.lower() == character.lower():
#         count += 1
#
# print("Count:", count)

# # 3. Given [10, 20, 30, 40, 50], find the sum of the first and last elements, then remove both elements from the list.
#
# n = [10, 20, 30, 40, 50]
# s = n[0]+n[-1]
# print(s)
# n.pop(0)
# n.pop()
# print(n)
#
# # By Chat GPT
# numbers = [10, 20, 30, 40, 50]
#
# total = numbers[0] + numbers[-1]
#
# numbers.pop(0)
# numbers.pop()
#
# print("Sum of first and last elements:", total)
# print("Updated list:", numbers)

# # 4. Given a dictionary of students and marks, print the names sorted by marks from highest to lowest.
# students = {"Ravi": 75, "Anu": 92, "Kiran": 85, "Meena": 68}
# f = {}
# for key,value in students.items():
#     value = max(value)
#
# # Correct One
# students = {"Ravi": 75, "Anu": 92, "Kiran": 85, "Meena": 68}
# sort = sorted(students.items(), key = lambda item: item[1], reverse=True)
#
# for name, marks in sort:
#     print(name,":",marks )

# # 5. Given "a1b2c3d4", replace each digit with its square.
# # Expected: "a1b4c9d16"
# a = "a1b2c3d4"
# d = 0
# for c in a:
#     if c.isdigit():
#         d = int(c)**2
#         c = d
# print(a)
#
# # Correct one
# a = "a1b2c3d4"
# r = ""
# for c in a:
#     if c.isdigit():
#         r += str(int(c)**2)
#     else:
#         r += c
# print(r)