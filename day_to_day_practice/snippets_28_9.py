# # 1.	Given [3, 1, 4, 1, 5, 9, 2], find the first repeated element.
#
# a = [3, 1, 4, 1, 5, 3, 9, 2]
# b = set()
# d = None
# for c in a:
#     if c in b:
#         d = c
#         break
#     b.add(c)
# print(d)

# # 2. Get a sentence and print the shortest word.
#
# s = "python is programming language and python is easy"
# # a = set(s.split())
# a = s.split()
# print(a)
# x = a[0]
# print(x)
# for c in a:
#     if len(c) < len(x):
#         x = c
# print(x)

# # 3. Given "Hello123World456", extract all digits and form the number 123456.
#
# a = "Hello123World456"
# d = ""
# for c in a:
#     if c.isdigit():
#         d += c
# print(d)

# # 4. Given a list of numbers, count how many are positive, negative, and zero.
#
# numbers = [4, -2, 0, 7, -5, 0, 3]
# p = 0
# n = 0
# z = 0
# for number in numbers:
#     if number > 0:
#         p += 1
#     elif number < 0:
#         n += 1
#     else:
#         z += 1
#
# print("Positive: ", p)
# print("Negative: ", n)
# print("Zeros: ", z)

# # 5. Given two dictionaries, find the keys that exist in both dictionaries.
#
# d1 = {"Brand":"Ford","Model":'Aspire',"Country":"England","Year":2024,"Continent":"Europe", "Color":"Red"}
# d2 = {"Country":"AUS","Format":'Test',"Matches":15, "Won":10, "Continent":"Australia"}
# # d3 = {} # for fetching key and values
# d3 = []
# for key,value in d1.items():
#     if key in d2:
#         d3.append(key)
#         # d3[key] = value
# print(d3)