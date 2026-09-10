## 1.	Given a list [2, 4, 6, 8, 10], find the sum of all elements using a loop.

# a = [2, 4, 6, 8, 10]
# d = 0
# for b in a:
#     d = b+d
#     # print(d)
# print(d)

# # 2.	Get a string from the user and count how many vowels it contains
#
# a = str(input())
# b = ['a','e','i','o','u']
# a.lower()
# if a in b:
#     print("It is a Vowel")
# else:
#     print("It is not a Vowel")

# # 3.	Given "madam", check whether it is a palindrome without using slicing ([::-1]).
#
# a = "madam"
# r=""
# for c in a:
#     r=c+r
# if r==a:
#     print("It is a Palindrome")
# else:
#     print("It is not a Palindrome")
# print(r)

# # 4.	Given [10, 20, 30, 40, 50], print the largest and smallest values.
#
# a = [10, 20, 30, 40, 50]
# a.sort()
# b = a[0]
# a.reverse()
# print(a[0])
# print(b)

# # 5.	Given [1, 2, 2, 3, 4, 4, 5], remove duplicate elements while keeping the original order.
#
# a = [1, 2, 2, 3, 4, 4, 5]
# s=set()
# d=[]
# for i in a:
#     if i in s and i not in d:
#         d.append(i)
#     else:
#         s.add(i)
# print(s)
# print(d)

# # 6.	Get a number from the user and print its multiplication table from 1 to 10.
#
# n = 10 # or n = int(input())
# for i in range(1,11):
#     print("{0} * {1} = {2}".format(n,i,n*i))

# # 7.	Given "automation testing automation", find the frequency of each word.
#
# a = "automation testing automation"
# f = {}
# b=a.split()
# for c in b:
#     if c in f:
#         f[c] += 1
#     else:
#         f[c] = 1
# print(f)

# # 8.	Given [1, 2, 3, 4, 5, 6], create a new list containing only even numbers.
#
# a = [1, 2, 3, 4, 5, 6]
# b = []
#
# for c in a:
#     if c%2 == 0:
#         b.append(c)
# print(b)

# # 9.	Given two lists [1, 2, 3] and [3, 4, 5], find elements that exist only in the first list.
#
# a = [1, 2, 3]
# b = [3, 4, 5]
#
# for c in a:
#     if c in a and c not in b:
#         print(c)

# # 10.	Given student records: Print the name(s) of students with the highest score.
#
# records = [["alpha", 80], ["beta", 95], ["theta", 95], ["gamma", 70]]
# s = max(record[1] for record in records )
# for name,marks in records:
#     if marks==s:
#         print(name)

# # 11.	Get a number from the user and check whether it is an Armstrong number. Example: 153 = 1³ + 5³ + 3³.
#
# n = int(input())
# o=n
# digits=len(str(n))
# s=0
#
# while n > 0:
#     d = n % 10
#     s += d**digits
#     n = n//10
# if s == o:
#     print("It is Armstrong number")
# else:
#     print("It is not an Armstrong number")

# # 12.	Given "aabbbcccc", compress it into a2b3c4.
#
# text = "aabbbcccc"
# compressed = ""
# count=1
#
# for i in range(1,len(text)):
#     if text[i] == text[i-1]:
#         count += 1
#     else:
#         compressed +=  text[i-1] + str(count)
#         count = 1
# compressed += text[i-1]+str(count)
# print(compressed)

