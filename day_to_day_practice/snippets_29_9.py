# # 1. Given [12, 5, 8, 12, 20, 5, 3], print each duplicate number only once.
# a = [12, 5, 8, 12, 20, 5, 3]
# s = set()
# d = []
# for c in a:
#     if c in s and c not in d:
#         d.append(c)
#     else:
#         s.add(c)
# print(s)
# # print(d)

# # 2. Get a string and count the number of words that are palindromes.
# # text = "madam level python civic code"
# # # Expected count: 3
#
# text = "madam level python civic code"
# t = text.split()
# # print(t)
# n = 0
# for c in t:
#     if c == c[::-1]:
#         n += 1
# print(n)

# # 3. Given [4, 9, 1, 7, 3], find the index of the largest element without using max().
#
# n = [4, 9, 1, 7, 3]
# s = 0
# for c in range(0,len(n)):
#     if n[c] > n[s]:
#         s = c
# print(s)

# # 4. Given a dictionary of items and quantities, print only items whose quantity is less than 10.
#
# inventory = {"Pen": 15, "Book": 5, "Bag": 8, "Pencil": 20}
# k = 0
# name = ""
# for key,value in inventory.items():
#     if value > k:
#         k = value
#         name = key
# print(name)

# # 5. Given "a1b2c3d4", separate letters and digits into two strings.
# # # Expected:
# # # letters = "abcd"
# # # digits = "1234"
#
# a = "a1b2c3d4"
# l = ""
# d = ""
# for c in a:
#     if c.isalpha():
#         l += c
#     elif c.isdigit():
#         d += c
# print(l)
# print(d)