# # 1. Given [2, 5, 2, 8, 5, 3], print only the elements that appear exactly once.
#
# a = [2, 5, 2, 8, 5, 3]
# s = set()
# d = []
# for i in a:
#     if i in s and i not in d:
#         d.append(i)
#     else:
#         s.add(i)
#
# n = []
# for c in s:
#     if c in s and c not in d:
#         n.append(c)
#
# print(s)
# print(n)

# # 2. Get a string and check whether all its characters are unique.
#
# a = str(input())
# u=True
# for i in a:
#     if a.count(i) > 1:
#         u=False
#
# if u==True:
#     print("unique char are present")
# else:
#     print("unique char are not present")

# # 3. Given a number, print the first n Fibonacci numbers.
# n = int(input())
# b,d = 0,1
# for i in range(n+1):
#     print(b)
#     b,d = d,b+d

# # 4.Given [4, 1, 7, 3, 9], find the second smallest distinct number.
# n = [4, 1, 7, 3, 9]
# n = set(n)
# b = sorted(n)
# print(b[1])

# # 5. Get a sentence and count how many words start with a vowel.
# s = "python is a programming language and python is easy"
# d = 0
# for i in s.split():
#     if i[0].lower() in "aeiou":
#         d  += 1
# print(d)

# # 6. Given [1, 2, 3, 4, 5], find all possible pairs whose product is even.
# a = [1, 2, 3, 4, 5]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if (a[i]*a[j])%2 == 0:
#             print(a[i],a[j])

# # 7. Given "aabbccdde", remove duplicate characters while keeping the first occurrence.
# a = "aabbccdde"
# s = ""
# for c in a:
#     if c not in s:
#         s += c
# print(s)

# # 8. Given a dictionary of student names and marks, print the student(s) who scored above the average.
# a = {"Madhu": 65, "Mahesh" : 75, "Suresh": 55,"Malli": 95}
# t = 0
# for marks in a.values():
#     t += marks
# average = t/len(a)
# print(average)
# for name,marks in a.items():
#     if marks > average:
#         print(name, ':', marks)

# # 9. Get a number and check whether it is a palindrome number. Example: 121.
# number = int(input("Enter a number: "))
#
# original_number = number
# reverse = 0
#
# while number > 0:
#     digit = number % 10
#     reverse = reverse * 10 + digit
#     number = number // 10
#
# if original_number == reverse:
#     print("Palindrome number")
# else:
#     print("Not a palindrome number")

# # 10. Given two lists, find common elements without using set().
# a = [6,1,4,3,2,1]
# b = [2,1,5,3,0,5]
# d = []
# for c in a:
#     if c in b and c not in d:
#         d.append(c)
# print(d)

# # 11. Given "Python123!", count alphabetic characters, numeric characters, and special characters.
# s = "Python123!"
# a = 0
# n = 0
# sc = 0
# for i in s:
#     if i.isalpha():
#         a += 1
#     elif i.isdigit():
#         n += 1
#     else:
#         sc += 1
#
# print(a)
# print(n)
# print(sc)

# # 12. Given a list of words, group words by their length. Example: words = ["cat", "dog", "apple", "bat", "car"]
# # Expected: {3: ["cat", "dog", "bat", "car"], 5: ["apple"]}
#
# words = ["cat", "dog", "apple", "bat", "car"]
# g = {}
#
# for word in words:
#     l = len(word)
#
#     if l not in g:
#         g[l] = []
#     g[l].append(word)
# print(g)