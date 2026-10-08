# # 1. Given [5, 10, 15, 20, 25], create a new list where each element is the difference from the previous element. Keep the first element unchanged.
# # Expected: [5, 5, 5, 5, 5]
# n = [5, 10, 15, 20, 25]
# l = []
# l.append(n[0])
# d = 0
# for i in range(len(n)):
#     for j in range(i+1,len(n)):
#         d = n[i+1]-n[i]
#         l.append(d)
#         break
# print(l)
#
# # By Chat GPT
# numbers = [5, 10, 15, 20, 25]
#
# result = [numbers[0]]
#
# for i in range(1, len(numbers)):
#     difference = numbers[i] - numbers[i - 1]
#     result.append(difference)
#
# print(result)
# # Output: [5, 5, 5, 5, 5]

# # 2. Get a string and print the first character that occurs exactly twice.
# a = input()
# for c in a:
#     if a.count(c) == 2:
#         print(c)
#         break
#
# # By Chat GPT
# text = input("Enter a string: ")
#
# for char in text:
#     if text.count(char) == 2:
#         print("First character occurring twice:", char)
#         break
# else:
#     print("No character occurs exactly twice")

# # 3. Given [1, 2, 3, 4, 5], move the first two elements to the end.
# # Expected: [3, 4, 5, 1, 2]
# n = [1, 2, 3, 4, 5]
# a = n[0]
# b = n[1]
# n.pop(0)
# n.pop(0)
# print(n)
# n.append(a)
# n.append(b)
# print(n)
#
# # By Chat GPT
# numbers = [1, 2, 3, 4, 5]
#
# a1 = numbers[:2]
# a2 = numbers[2:]
# r = a2+a1
# print(r)

# # 4. Given a dictionary of employees and salaries, calculate the average salary and print the employees earning above average.
# salaries = {"Ravi": 40000, "Anu": 60000, "Kiran": 50000, "Meena": 75000}
# avg = 0
# sum = 0
# for key,value in salaries.items():
#     sum += value
#     # print(sum)
#     avg = sum/len(salaries)
# for key, value in salaries.items():
#     if value > avg:
#         print(key,value)
#
# # By Chat GPT
# salaries = {
#     "Ravi": 40000,
#     "Anu": 60000,
#     "Kiran": 50000,
#     "Meena": 75000
# }
#
# total_salary = 0
#
# for salary in salaries.values():
#     total_salary += salary
#
# average_salary = total_salary / len(salaries)
#
# print("Average salary:", average_salary)
#
# for employee, salary in salaries.items():
#     if salary > average_salary:
#         print(employee, ":", salary)

# # 5. Given "A man a plan a canal Panama", check whether it is a palindrome while ignoring spaces and case.
# a = "A man a plan a canal Panama"
# a = a.lower()
# a = a.replace(" ", "")
# print(a)
# b = a[::-1]
# print(b)
#
# if a==b:
#     print("It is a Palindrome")
# else:
#     print("It is not a Palindrome")
#
# # By Chat GPT
# text = "A man a plan a canal Panama"
#
# cleaned_text = ""
#
# for char in text:
#     if char != " ":
#         cleaned_text += char.lower()
#
# if cleaned_text == cleaned_text[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")