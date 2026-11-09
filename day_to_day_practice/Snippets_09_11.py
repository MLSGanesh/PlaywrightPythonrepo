# # 1. Given [1, 2, 3, 4, 5, 6], find the first pair of adjacent elements whose sum is greater than 8.
# n = [1, 2, 3, 4, 5, 6]
# for i in range(1,len(n)):
#     if n[i]+n[i-1] > 8:
#         print(n[i],n[i-1])
#         break
#
# # By ChatGPT
# numbers = [1, 2, 3, 4, 5, 6]
#
# for i in range(len(numbers) - 1):
#     if numbers[i] + numbers[i + 1] > 8:
#         print("First pair:", numbers[i], numbers[i + 1])
#         break

# # 2. Get a sentence and print the word that occurs most often. If there is a tie, print the word that appears first.
# a = "I like cricket and like playing cricket"
#
# # Correct One
# sentence = input("Enter a sentence: ").lower()
#
# words = sentence.split()
# frequency = {}
#
# for word in words:
#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1
#
# most_frequent_word = ""
# highest_count = 0
#
# for word in words:
#     if frequency[word] > highest_count:
#         highest_count = frequency[word]
#         most_frequent_word = word
#
# print("Most frequent word:", most_frequent_word)
# print("Count:", highest_count)

# # 3. Given [4, 7, 2, 9, 5], replace every element with the difference between the largest element and itself.
# # Expected: [5, 2, 7, 0, 4]
# n = [4, 7, 2, 9, 5]
# h = 0
# for i in n:
#     if i > h:
#         h = i
# for j in range(0,len(n)):
#     n[j] = h-n[j]
# print(n)
#
# # By ChatGPT
# numbers = [4, 7, 2, 9, 5]
#
# largest = numbers[0]
#
# for number in numbers:
#     if number > largest:
#         largest = number
#
# result = []
#
# for number in numbers:
#     result.append(largest - number)
#
# print(result)
# # Output: [5, 2, 7, 0, 4]

# 4. Given a dictionary of products and prices, print the product with the second-lowest distinct price.
prices = {"Pen": 10, "Book": 50, "Bag": 500, "Pencil": 10, "Scale": 20}
for key, value in prices.items():
     m = max(value)
