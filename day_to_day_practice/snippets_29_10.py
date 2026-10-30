# # 1. Given [4, 7, 1, 9, 3, 6], print all elements that are greater than both their immediate neighbors.
# n = [4, 7, 1, 9, 3, 6]
# for i in range(0,len(n)):
#     for j in range(1,len(n)):
#         for k in range(j+1,len(n)):
#             if n[j] > n[i] and n[j] > n[k]:
#                 print(n[j])
#                 break
#
# # By ChatGPT
# n = [4, 7, 1, 9, 3, 6]
# for i in range(1,len(n)-1):
#     if n[i] > n[i-1] and n[i] > n[i+1]:
#         print(n[i])

# # 2. Get a string and print the first word that has the maximum length.
# # Example: "I love learning Python programming" → "programming".
# a = "I love learning Python programming"
# a = a.split()
# b = 0
# for c in a:
#     if len(c) > b:
#         b = len(c)
# print(c)
#
# # By ChatGPT
# text = input("Enter a sentence: ")
#
# words = text.split()
#
# longest_word = words[0]
#
# for word in words:
#     if len(word) > len(longest_word):
#         longest_word = word
#
# print("First longest word:", longest_word)

# # 3. Given [1, 2, 3, 4, 5], replace each element with the sum of itself and the next element. Keep the last element unchanged.
# # Expected: [3, 5, 7, 9, 5]
# n = [1, 2, 3, 4, 5]
# for i in range(0,len(n)-1):
#     n[i] = n[i]+n[i+1]
# print(n)
#
# # By ChatGPT
# numbers = [1, 2, 3, 4, 5]
#
# result = []
#
# for i in range(len(numbers) - 1):
#     result.append(numbers[i] + numbers[i + 1])
#
# result.append(numbers[-1])
#
# print(result)
# # Output: [3, 5, 7, 9, 5]

# # 4. Given a dictionary of students and their marks, find the difference between the highest and lowest mark.
# marks = {"Ravi": 75, "Anu": 92, "Kiran": 68, "Meena": 85}
# d = []
# for value in marks.values():
#     d.append(value)
# print(max(d)-min(d))
#
# # By ChatGPT
# marks = {
#     "Ravi": 75,
#     "Anu": 92,
#     "Kiran": 68,
#     "Meena": 85
# }
#
# highest_mark = 0
# lowest_mark = float("inf")
#
# for mark in marks.values():
#     if mark > highest_mark:
#         highest_mark = mark
#
#     if mark < lowest_mark:
#         lowest_mark = mark
#
# difference = highest_mark - lowest_mark
#
# print("Difference:", difference)
# # Output: 24

# # 5. Given "aabbccabc", print the characters in the order they first become repeated.
# # Expected: a, b, c
# a = "aabbccabc"
# a = list(a)
# for c in a:
#     if a.count(c) > 1:
#         print(c)
#
# # Correct One
# a = "aabbccabc"
# s = set()
# d = []
# for c in a:
#     if c in s and c not in d:
#         d.append(c)
#     else:
#         s.add(c)
# for c in d:
#     print(c)