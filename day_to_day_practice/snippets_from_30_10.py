# # 1. Given [2, 4, 6, 8, 10], check whether each element is double the previous element.
# n = [2, 4, 6, 8, 10]
# for i in range(1,len(n)):
#     if n[i] == 2*n[i-1]:
#         print("Double the Previous one: ",n[i])
#     else:
#         print("Not a Double of Previous one")
#
# # By ChatGPT
# numbers = [2, 4, 6, 8, 10]
#
# is_double = True
#
# for i in range(1, len(numbers)):
#     if numbers[i] != numbers[i - 1] * 2:
#         is_double = False
#         break
#
# if is_double:
#     print("Each element is double the previous element")
# else:
#     print("Not every element is double the previous element")

# # 2. Get a sentence and print the word with the second-longest distinct length.
# a = "I love learning Python programming"
# a = list(a)
#
# l = 0
# t = []
# for c in a:
#     if len(c) > l:
#         l = len(c)
#         t.append(c)
#
# # Correct One
# a = "I love learning Python programming"
# a = a.split()
# l = []
# for c in a:
#     if len(c) not in l:
#         l.append(len(c))
# l.sort(reverse=True)
# if len(l) >= 2:
#     sl = l[1]
# for d in a:
#     if len(d) == sl:
#         print(d)

# # 3. Given [3, 1, 4, 1, 5, 9], create a new list containing the running maximum.
# # Expected: [3, 3, 4, 4, 5, 9]
# n = [3, 1, 4, 1, 5, 9]
# d = []
# s = 0
# for i in range(1,len(n)):
#     for j in range(0,len(n)-1):
#         if n[i] >= n[j]:
#             d.append(n[i])
#             s = n[i]
#         else:
#             d.append(s)
#         print(d)
# print(d)
#
# # Correct One
# n = [3, 1, 4, 1, 5, 9]
# r = []
# m = n[0]
# for i in n:
#     if i > m:
#         m = i
#     r.append(m)
# print(r)

# # 4. Given a dictionary of employees and their working hours, print the employee(s) who worked the most hours.
# hours = {"Ravi": 40, "Anu": 45, "Kiran": 45, "Meena": 38}
# m = 0
# for value in hours.values():
#     if value > m:
#         m = value
#
# for key, value in hours.items():
#     if value == m:
#         print(key)
#
# # By ChatGPT
# hours = {
#     "Ravi": 40,
#     "Anu": 45,
#     "Kiran": 45,
#     "Meena": 38
# }
#
# highest_hours = 0
#
# for worked_hours in hours.values():
#     if worked_hours > highest_hours:
#         highest_hours = worked_hours
#
# for employee, worked_hours in hours.items():
#     if worked_hours == highest_hours:
#         print(employee, ":", worked_hours)

# # 5. Given "abc123def45", separate the letters, digits, and count of each type.
# a = "abc123def45"
# l = []
# d = []
# for c in a:
#     if c.isdigit():
#         d.append(c)
#     elif c.isalpha():
#         l.append(c)
#
# d = "".join(d)
# l = "".join(l)
# print(l)
# print(d)
# print("Count of Letters: ",len(l))
# print("Count of Digits: ",len(d))
#
# # By ChatGPT
# text = "abc123def45"
#
# letters = ""
# digits = ""
#
# for char in text:
#     if char.isalpha():
#         letters += char
#     elif char.isdigit():
#         digits += char
#
# print("Letters:", letters)
# print("Digits:", digits)
# print("Letter count:", len(letters))
# print("Digit count:", len(digits))