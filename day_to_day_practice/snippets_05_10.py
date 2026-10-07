# # 1. Given [2, 3, 4, 5, 6, 7], create a list containing the squares of only the odd numbers.
# n = [2, 3, 4, 5, 6, 7]
# l = []
# for i in n:
#     if i%2 == 1:
#         l.append(i**2)
# print(l)
#
# # By Chat GPT
# numbers = [2, 3, 4, 5, 6, 7]
#
# odd_squares = []
#
# for number in numbers:
#     if number % 2 != 0:
#         odd_squares.append(number ** 2)
#
# print(odd_squares)
# # Output: [9, 25, 49]

# # 2. Get a string and print the first word that appears more than once.
# a = "the python is a language and python is easy to learn"
# b = a.split()
# d = []
# for c in b:
#     if c not in d:
#         d.append(c)
#         if c in d:
#             print(c)
#
# # Correct One
# a = "the python is a language and python is easy to learn"
# b = a.split()
# s = set()
# for c in b:
#     if c in s:
#         print(c)
#         break
#     s.add(c)

# # 3. Given [1, 4, 9, 16, 25], check whether every element is a perfect square.
# n = [1, 4, 9, 16, 25]
# s = 0
# for i in n:
#     s = i**0.5
#     if s**2 == i:
#         print("It is a Perfect Square")
#     else:
#         print("Not a Perfect square")
#
# # By Chat GPT
# numbers = [1, 4, 9, 16, 25]
#
# all_perfect_squares = True
#
# for number in numbers:
#     root = int(number ** 0.5)
#
#     if root * root != number:
#         all_perfect_squares = False
#         break
#
# if all_perfect_squares:
#     print("All elements are perfect squares")
# else:
#     print("Not all elements are perfect squares")

# # 4. Given a dictionary of products and prices, print the total price of all products.
# prices = {"Pen": 10, "Book": 50, "Bag": 500, "Pencil": 5}
# Total = 0
# for key,value in prices.items():
#     Total += value
# print(Total)
#
# # By Chat GPT
# prices = {
#     "Pen": 10,
#     "Book": 50,
#     "Bag": 500,
#     "Pencil": 5
# }
#
# total_price = 0
#
# for price in prices.values():
#     total_price += price
#
# print("Total price:", total_price)
# # Output: 565

# # 5. Given "aaabbbbccdaa", find the longest sequence of consecutive same characters.
# # Expected: bbbb
# s = "aaabbbbccdaa"
# n = 1
# for c in s:
#     if s.count(c) == n:
#         n += 1
#         print(n)
#
# # Correct one
# text = "aaabbbbccdaa"
#
# longest_sequence = ""
# current_sequence = ""
#
# for char in text:
#     if char == current_sequence[:1]:
#         current_sequence += char
#     else:
#         current_sequence = char
#
#     if len(current_sequence) > len(longest_sequence):
#         longest_sequence = current_sequence
#
# print("Longest sequence:", longest_sequence)
# # Output: bbbb




