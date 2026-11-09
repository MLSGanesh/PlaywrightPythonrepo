# # 1. Given [5, 2, 8, 2, 9, 5, 1], find the element that has the highest frequency. If there is a tie, print the one that appears first.
# n = [5, 2, 8, 2, 9, 5, 1]
# d = []
# a = []
# s = set()
# # for e in range(0,len(n)):
# for i in n:
#         if i in s and i not in d:
#             d.append(i)
#             # a.insert(e,i)
#         else:
#             s.add(i)
# print(d)
# # print(a)
# print(s)
#
# # Correct one
# n = [5, 2, 8, 2, 9, 5, 1]
# f = {}
# for i in n:
#     if i in f:
#         f[i] += 1
#     else:
#         f[i] = 1
# h = 0
# m = None
# for i in n:
#     if f[i] > h:
#         h = f[i]
#         m = i
# print(m)
# print(h)

# # 2. Get a sentence and count how many words have more than 5 characters.
# a = "I like Cricket and love playing the game"
# b = a.split()
# d = list(b)
# n = 0
# print(d)
# for c in d:
#     if len(list(c)) >= 5:
#         n += 1
# print(n)
#
# # By ChatGPT
# sentence = input("Enter a sentence: ")
#
# count = 0
#
# for word in sentence.split():
#     if len(word) > 5:
#         count += 1
#
# print("Words with more than 5 characters:", count)

# # 3. Given [10, 20, 30, 40, 50], insert the average of the list at index 2.
# n = [10, 20, 30, 40, 50]
# total = 0
# for i in n:
#     if i > 0:
#         total += i
# print(total)
# print(len(n))
# avg = total//len(n)
# n.insert(2,avg)
# print(n)
#
# # By ChatGPT
# numbers = [10, 20, 30, 40, 50]
#
# total = 0
#
# for number in numbers:
#     total += number
#
# average = total / len(numbers)
#
# numbers.insert(2, average)
#
# print(numbers)
# # Output: [10, 20, 30.0, 30, 40, 50]

# # 4. Given a dictionary of students and marks, create a new dictionary containing only students with marks between 50 and 80, inclusive.
# students = {"Ravi": 45, "Anu": 78, "Kiran": 85, "Meena": 65}
# dict = {}
# for key,value in students.items():
#     if value >= 50 and value <= 80:
#         dict[key] = value
# print(dict)
#
# # By ChatGPT
# students = {
#     "Ravi": 45,
#     "Anu": 78,
#     "Kiran": 85,
#     "Meena": 65
# }
#
# filtered_students = {}
#
# for name, marks in students.items():
#     if 50 <= marks <= 80:
#         filtered_students[name] = marks
#
# print(filtered_students)

# # 5. Given "a1b22c333", print each digit along with how many consecutive times it occurs.
# # Expected: 1 → 1, 2 → 2, 3 → 3
# n = "a1b22c333"
# a = list(n)
# count = 0
# for i in range(1,len(n)):
#     for j in range(i-1,len(n)):
#         if n[j].isdigit() and n[i]==n[j]:
#             count += 1
#             print(n[i],"->",count)
#             break
#
# # Correct One
# text = "a1b22c333"
#
# current_digit = ""
# count = 0
#
# for char in text:
#     if char.isdigit():
#         if char == current_digit:
#             count += 1
#         else:
#             if current_digit != "":
#                 print(current_digit, "→", count)
#
#             current_digit = char
#             count = 1
#     else:
#         if current_digit != "":
#             print(current_digit, "→", count)
#             current_digit = ""
#             count = 0
#
# if current_digit != "":
#     print(current_digit, "→", count)
