# # 1. Given [3, 1, 4, 1, 5, 9, 2], find the first element greater than the average of the list.
# n = [3, 1, 4, 1, 5, 9, 2]
# print(len(n))
# a = 0
# for i in n:
#     a = a+i
#     # print(a)
# print(a)
# for j in n:
#     if j > (a%(len(n))):
#         print(j)
#         break
#
# # By ChatGPT
# numbers = [3, 1, 4, 1, 5, 9, 2]
#
# total = 0
#
# for number in numbers:
#     total += number
#
# average = total / len(numbers)
#
# for number in numbers:
#     if number > average:
#         print("First element greater than average:", number)
#         break

# # 2. Get a string and print the words that occur exactly once.
# text = "python is easy and python is powerful"
# for c in text:
#     if text.count(c) == 1:
#         print(c)
#
# # Correct one
# text = "python is easy and python is powerful"
# w = text.split()
# for c in w:
#     if w.count(c) == 1:
#         print(c)

# # 3. Given [1, 2, 3, 4, 5], create a new list where each element is multiplied by its index.
# # Expected: [0, 2, 6, 12, 20]
# a = [1, 2, 3, 4, 5]
# for i in range(0,len(a)):
#     a[i] = i*a[i]
# print(a)
#
# # By ChatGPT
#
# numbers = [1, 2, 3, 4, 5]
#
# result = []
#
# for index in range(len(numbers)):
#     result.append(numbers[index] * index)
#
# print(result)
# # Output: [0, 2, 6, 12, 20]

# # 4. Given a dictionary of products and quantities, print the product(s) with the highest quantity.
# inventory = {"Pen": 15, "Book": 20, "Bag": 20, "Pencil": 10}
# v = 0
# for key,value in inventory.items():
#     max(value)
#         print(key)
#
# # Correct One
# inventory = {"Pen": 15, "Book": 20, "Bag": 20, "Pencil": 10}
# v = 0
# for value in inventory.values():
#     if value > v:
#         v = value
# for key,value in inventory.items():
#     if value == v:
#         print(key)

# # 5. Given "aabbccddeeff", remove every second occurrence of each character.
# # Expected: "abcdef"
# a = "aabbccddeeff"
# a = set(a)
# a = sorted(a)
# b = "".join(a)
# print(b)
#
# # By ChatGPT
#
# text = "aabbccddeeff"
#
# result = ""
# seen = set()
#
# for char in text:
#     if char not in seen:
#         result += char
#         seen.add(char)
#
# print(result)
# # Output: abcdef









