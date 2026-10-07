# # 1. Given [1, 2, 3, 4, 5, 6], split the numbers into two lists: one for even numbers and one for odd numbers.
# n = [1, 2, 3, 4, 5, 6]
# e = []
# o = []
# for i in n:
#     if i%2 == 1:
#         o.append(i)
#     elif i%2 == 0:
#         e.append(i)
# print(e)
# print(o)
#
# # By Chat GPT
# numbers = [1, 2, 3, 4, 5, 6]
#
# even_numbers = []
# odd_numbers = []
#
# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)
#     else:
#         odd_numbers.append(number)
#
# print("Even numbers:", even_numbers)
# print("Odd numbers:", odd_numbers)

# # 2. Get a string and check whether it has balanced parentheses.
# # Example: "(a + b) * (c - d)" is balanced.
# # Correct One
# text = input("Enter a string: ")
#
# count = 0
# is_balanced = True
#
# for char in text:
#     if char == "(":
#         count += 1
#     elif char == ")":
#         count -= 1
#
#         if count < 0:
#             is_balanced = False
#             break
#
# if count == 0 and is_balanced:
#     print("Balanced parentheses")
# else:
#     print("Not balanced parentheses")

# # 3. Given [4, 2, 7, 2, 9, 4, 1], find the first element that appears only once.
# n = [4, 2, 7, 2, 9, 4, 1]
# d = []
# s = set()
# for i in n:
#     if i in s and i not in d:
#         d.append(i)
#     else:
#         s.add(i)
# print(d)
# print(s)
#
# # Correct One
# n = [4, 2, 7, 2, 9, 4, 1]
# for i in n:
#     if n.count(i) == 1:
#         print(i)
#         break

# # 4. Given a dictionary of cities and temperatures, print the city with the lowest temperature.
#
# temperatures = {"Hyderabad": 32, "Delhi": 28, "Bengaluru": 24, "Mumbai": 30}
# t = 0
# for key,value in temperatures.items():
#     if value.
#
# # Correct One
# temperatures = {"Hyderabad": 32, "Delhi": 28, "Bengaluru": 24, "Mumbai": 30}
#
# city = ""
# l_temp = float("inf")
# for key,value in temperatures.items():
#     if value < l_temp:
#         l_temp = value
#         city = key
# print(city)
# print(l_temp)

# # 5. Given "python,java,testing,automation", split the text by commas and print each value on a new line.
#
# a = "python,java,testing,automation"
#
# b = a.split(",")
# for c in b:
#     print(c)
