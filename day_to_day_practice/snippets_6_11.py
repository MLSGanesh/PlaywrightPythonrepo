# # 1. Given [2, 4, 6, 8, 10], find the first number that is greater than the sum of all previous numbers.
# n = [2, 4, 6, 8, 10]
# d = []
# for i in range(1,len(n)):
#     d.append(n[i-1])
#     if n[i]>sum(d):
#         print(n[i])
#
# # By ChatGPT
# numbers = [2, 4, 6, 8, 10]
#
# sum_of_previous = numbers[0]
#
# for i in range(1, len(numbers)):
#     if numbers[i] > sum_of_previous:
#         print("First number:", numbers[i])
#         break
#
#     sum_of_previous += numbers[i]

# # 2. Get a sentence and print all words that start and end with the same letter, ignoring case.
# a = "Hi Madam how are you refer to collection stats of tenet"
# b = a.split()
# for c in b:
#     if c.casefold() == c[::-1].casefold():
#         print(c)
#
# # By ChatGPT
# sentence = input("Enter a sentence: ")
#
# for word in sentence.split():
#     if word[0].lower() == word[-1].lower():
#         print(word)

# # 3. Given [1, 3, 5, 7, 9], insert 6 before the first element greater than 6.
# n = [1, 3, 5, 7, 9]
# for i in range(1,len(n)):
#     if n[i] > 6:
#         n.insert(i-1,6)
#         break
# print(n)
#
# # By ChatGPT
# numbers = [1, 3, 5, 7, 9]
# new_number = 6
#
# for i in range(len(numbers)):
#     if numbers[i] > new_number:
#         numbers.insert(i, new_number)
#         break
#
# print(numbers)
# # Output: [1, 3, 5, 6, 7, 9]

# # 4. Given a dictionary of employees and salaries, increase each salary by 10% and create a new dictionary.
# salaries = {"Ravi": 40000, "Anu": 60000, "Kiran": 50000}
# new = {}
# for key,value in salaries.items():
#     new[key] = value*110//100
# print(new)
#
# # By ChatGPT
# salaries = {
#     "Ravi": 40000,
#     "Anu": 60000,
#     "Kiran": 50000
# }
#
# updated_salaries = {}
#
# for employee, salary in salaries.items():
#     updated_salaries[employee] = salary * 1.10
#
# print(updated_salaries)

# # 5. Given "aabbbbccdddde", print the character(s) with the longest consecutive sequence.
# a = "aabbbbccdddde"
# n = 0
# for i in range(1,len(a)):
#     if a[i] == a[i-1]:
#         n += 1
#         print(n)
#
# # Correct One
# text = "aabbbbccdddde"
#
# longest_count = 0
# current_count = 1
# longest_characters = []
#
# for i in range(1, len(text)):
#     if text[i] == text[i - 1]:
#         current_count += 1
#     else:
#         if current_count > longest_count:
#             longest_count = current_count
#             longest_characters = [text[i - 1]]
#         elif current_count == longest_count:
#             longest_characters.append(text[i - 1])
#
#         current_count = 1
#
# # Check the final sequence
# if current_count > longest_count:
#     longest_count = current_count
#     longest_characters = [text[-1]]
# elif current_count == longest_count:
#     longest_characters.append(text[-1])
#
# print("Characters:", longest_characters)
# print("Longest consecutive count:", longest_count)

# # 1. Given [4, 1, 6, 3, 8, 2], find the sum of elements that are greater than the previous element.
# n = [4, 1, 6, 3, 8, 2]
# s = 0
# for i in range(1,len(n)):
#     if n[i] > n[i-1]:
#         s += n[i]
# print(s)
#
# # By ChatGPT
# numbers = [4, 1, 6, 3, 8, 2]
#
# total = 0
#
# for i in range(1, len(numbers)):
#     if numbers[i] > numbers[i - 1]:
#         total += numbers[i]
#
# print("Sum:", total)
# # Output: 14

# # 2. Get a sentence and print the first word that contains all unique characters.
# a = "cricket loved add by me"
# b = a.split()
# l = []
# for c in b:
#     for d in c:
#         if c.count(d) == 1:
#             print(c)
#         else:
#             print("")
#
# # Correct One
# sentence = input("Enter a sentence: ")
#
# for word in sentence.split():
#     is_unique = True
#
#     for char in word.lower():
#         if word.lower().count(char) > 1:
#             is_unique = False
#             break
#
#     if is_unique:
#         print("First word with unique characters:", word)
#         break
# else:
#     print("No word has all unique characters")

# # 3. Given [2, 4, 6, 8, 10], replace each element with the product of itself and the previous element. Keep the first element unchanged.
# # Expected: [2, 8, 24, 48, 80]
# n = [2, 4, 6, 8, 10]
# l = [n[0]]
# for i in range(1,len(n)):
#     l.append(n[i]*n[i-1])
# print(l)
#
# # By ChatGPT
# numbers = [2, 4, 6, 8, 10]
#
# result = [numbers[0]]
#
# for i in range(1, len(numbers)):
#     product = numbers[i] * numbers[i - 1]
#     result.append(product)
#
# print(result)
# # Output: [2, 8, 24, 48, 80]

# # 4. Given a dictionary of students and marks, print the names of students who have the same marks.
# students = {"Ravi": 85, "Anu": 92, "Kiran": 85, "Meena": 78, "Priya": 92}
#
# for key,value in students.items():
#     for i in range(0,len(students.values())):
#         if len(i)>:
#           print(key)
#
# # Correct One
# students = {
#     "Ravi": 85,
#     "Anu": 92,
#     "Kiran": 85,
#     "Meena": 78,
#     "Priya": 92
# }
#
# same_marks = {}
#
# for name, mark in students.items():
#     if mark not in same_marks:
#         same_marks[mark] = []
#
#     same_marks[mark].append(name)
#
# for mark, names in same_marks.items():
#     if len(names) > 1:
#         print("Marks:", mark, "| Students:", names)

# # 5. Given "abcabcabcd", find the shortest prefix that repeats at least twice.
# a = "abcabcabcd"
# # Correct One
# text = "abcabcabcd"
#
# for length in range(1, len(text) + 1):
#     prefix = text[:length]
#
#     if text.count(prefix) >= 2:
#         print("Shortest repeating prefix:", prefix)
#         break