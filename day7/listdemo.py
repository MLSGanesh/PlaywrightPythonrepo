# Creating list

# mylist1 = [10,20,30,40,50]
# mylist2 = ["Mango", "Apple","Cherry"]
# mylist3 = [10,"Mango", "A",True]
#
# mylist4 = list() # this will create empty list
#
# print(mylist1)
# print(mylist2)
# print(mylist3)
# print(mylist4) # []


# Access items/values/objects from the list
# mylist = ["Mango", "Apple","Cherry"] # index starts from 0
# print(mylist[0]) # Mango
# print(mylist[2]) # Cherry
# print(mylist[-1]) # Cherry -neg value starts from last
# print(mylist[-3])
# print(mylist[-2])

# Access multiple values from the list (range of indexes)
# mylist = ["Mango", "Apple","Cherry", "Orange", "Kiwi", "Papaya", "Watermelon", "Guava"]
# print(mylist[3:5])
# print(mylist[-5:-1])
# print(mylist[-5:])

# change the value in the list
# mylist = ["Mango", "Apple","Cherry"]
# print("Before the change: ",mylist)
# mylist[0] = "Banana"
# print("After the change: ",mylist)

# loop with list
# Example 1:
# mylist = ["Mango", "Apple","Cherry"]
# for i in mylist:
#     print(i)

# check if an item exists in list (searching an item)
# mylist = ["Mango", "Apple","Cherry"]
#
# if "Apple" in mylist:
#     print("Yes, Apple is exist")
# else:
#     print("No, Apple doen't exist")

# for i in mylist:
#     if i=="Apple":
#         print(i)

# find out length/size of the list
#
# str="welcome"
# print(len(str))
#
# mylist = ["Mango", "Apple","Cherry"]
# print(len(mylist))

# count number of times the value is repeated in list
# mylist = ["Mango", "Apple","Cherry", "Apple", "Apple"]
# print(mylist.count("Apple"))

# sorting the list
# mylist = ["Mango", "Apple","Cherry", "Orange", "Kiwi", "Papaya", "Watermelon", "Guava"]
# print("Original list: ", mylist)
# # mylist.sort() # sorts the elements in ascending order
# mylist.sort(reverse=True) # sorts the elements in descending order
# print("Sorted list of values: ", mylist)

# Reversing list items
# pre-requisites values must be in sorted order
# mylist = ['Apple', 'Cherry', 'Guava', 'Kiwi', 'Mango', 'Orange', 'Papaya', 'Watermelon']
# print("Original values: ",mylist)
# mylist.reverse()
# print("Reversed values in a list: ", mylist)

# add item  append()  insert()
# mylist = ['Apple', 'Cherry', 'Guava']
# print("Before append: ",mylist)
# mylist.append("Orange") # at a time user can append only one value
# print("After append: ",mylist)
#
# mylist = ['Apple', 'Cherry', 'Guava']
# print("Before insert: ",mylist)
# mylist.insert(1,"Lemon")
# print("After insert: ",mylist)

# remove item from the list

# Approach 1: remove()
# mylist = ['Apple', 'Cherry', 'Guava', 'Kiwi', 'Mango', 'Orange', 'Papaya', 'Watermelon']
# mylist.remove("Kiwi")
# print("After removing: ",mylist)

# Approach 2: pop() accepts index
# mylist = ['Apple', 'Cherry', 'Guava', 'Kiwi', 'Mango', 'Orange', 'Papaya', 'Watermelon']
# mylist.pop(4)
# print("After removing: ",mylist)

# Approach 3: del
# mylist = ['Apple', 'Cherry', 'Guava', 'Kiwi', 'Mango', 'Orange', 'Papaya', 'Watermelon']
# del mylist[2] # we passed index of the element, as del is not a method it is a identifier/keyword
# print("After Removing: ",mylist)

# Deleting the list
# mylist = ['Apple', 'Cherry', 'Guava', 'Kiwi', 'Mango', 'Orange', 'Papaya', 'Watermelon']
# del mylist
# print("After Removing: ",mylist)

# Copying the list

# Approach 1: copy()
# mylist1 = ['Apple', 'Cherry', 'Guava', 'Kiwi', 'Mango', 'Orange', 'Papaya', 'Watermelon']
# mylist2 = mylist1.copy()
# print(mylist1)
# print(mylist2)

# Approach 1: list()
# mylist1 = ['Apple', 'Cherry', 'Guava', 'Kiwi', 'Mango', 'Orange', 'Papaya', 'Watermelon']
# mylist2 = list(mylist1)
# print(mylist1)
# print(mylist2)

# Join the lists

# Appraoch 1: using '+' operator
# list1=['a','b','c']
# list2=[1,2,3]
# list3=list1+list2
# print(list3)

# Approach 2: using looping statements
# list1=['a','b','c','d']
# list2=[1,2,3]
# list3=[]
# for i in list2:
#     list1.append(i)
#
# print(list1)


# Approach 3: using extend() method
# list1=['a','b','c','d']
# list2=[1,2,3]
# list1.extend(list2)
# print(list1)


# using looping statements adding third list
# list1=['a','b','c','d']
# list2=[1,2,3]
# list3=[]
# for i in list2:
#     list1.append(i)
#
# print(list1)
#
# for i in list1:
#     list3.append(i)
# for i in list2:
#     list3.append(i)
# print(list3)

a=[0,1,2,3,6]
d = set()
for i in a:
    if i%2==1:
        d.add(i)
        print(d)


# asked by Chatgpt

# items = ["Laptop", "Mouse", "", "keyboard", "Laptop", "  "]
# # Requirements:
# # - Remove empty or whitespace-only strings.
# # - Remove duplicate products.
# # - Convert each valid product name to title case.
# # - Return the final list in the same order of first appearance.
#
# valid_items = []
# seen_items = set()
#
# for item in items:
#         cleaned_item = item.strip()
#         print(cleaned_item)
#         if not cleaned_item:
#             continue
#
#         product = cleaned_item.title()
#         print(product)
#
#         if product not in seen_items:
#             valid_items.append(product)
#             seen_items.add(product)
#         print(valid_items)
#         print(seen_items)

