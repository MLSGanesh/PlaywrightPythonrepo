# creating set
# myset1 ={10,20,30,40,50}
# myset2={"apple", "banana", "cherry"}
# myset3={100,"A",True,'Welcome'}
# myset ={}
#
# print(myset1) # will print data in random order as set is unordered in nature
# print(myset2)
# print(myset3)
# print(myset)
from traceback import print_tb

# Accessing the values from a set
# User can not access values/items by using index(Set doesn't support index)
# User can not change values/items in set as index in not available, but can add new items.

# Access data from set using for loop
# myset = {"apple", "banana", "cherry"}
# for i in myset:
#     print(i)

# searching value/item in the set
# myset = {"apple", "banana", "cherry"}
# print("apple" in myset)
# print("Orange" in myset)
#
# if "apple" in myset:
#     print("Exists")
# else:
#     print("Not exists")

# Find the length/number of values in set
# myset = {'apple','banana',"cherry"}
# print(len(myset))

# Counting the elements is not possible, as duplicates are not allowed
# Sorting the elements is not possible, as set is unordered.
# Reversing the elements is not possible, as set is unordered.

# Add items/values into set
# add() - we can add single value
# update - we can add multiple values
# insert() - insertion is not possible as index is not present

# myset = {'apple','banana',"cherry"}
# myset.add("Orange")
# print("After adding: ",myset)

# myset = {'apple','banana',"cherry"}
# myset.update(["Orange",'Grapes'])
# print("After updating: ",myset)

# Added duplicates will get ingnored as duplicates ar enot allowed
# myset={1,2,3,3,4,4,5,8,8}
# print(myset)

# Removing values/items from set
# Approach 1: using remove()
# myset = {'apple','banana',"cherry"}
# # myset.remove("cherry")
# myset.remove("123") # key error
# print("After removing: ",myset)

# Approach 2: using discard()
# myset = {'apple','banana',"cherry"}
# myset.discard("cherry")
# myset.discard("123") # No error of value is not exists
# print("After removing: ",myset)

# Approach 3: pop(): removes random value/item from the set
# myset = {'apple','banana',"cherry"}
# myset.pop()
# print("After removing: ",myset)

# Clearing values from set
# myset = {'apple','banana',"cherry"}
# myset.clear()
# print("After clearing: ",myset)

# delete values from set
# myset = {'apple','banana',"cherry"}
# del myset
# print("After deletion: ",myset) # name error as set got deleted and nothing to print.

# copying the set

# Appoach 1: copy()
# myset1= {'apple','banana',"cherry"}
# myset2= myset1.copy()
# print(myset1)
# print(myset2)

# Approach 2: set()
# myset1= {'apple','banana',"cherry"}
# myset2= myset1
# myset2= set(myset1)
# print(myset1)
# print(myset2)

# Joining of sets
# Approach 1: using union()
# myset1={'a','b','c'}
# myset2={10,20,30}
#
# myset3=myset1.union(myset2)
# print(myset3)

# Approach 2: using '|' symbol
# myset1={'a','b','c'}
# myset2={10,20,30}
#
# myset3=myset1|myset2
# print(myset3)

# Retreiving common values from 2 sets

myset1={'a','b','c',10}
myset2={10,20,30,'a'}

# Approach 1: using intersection()
# myset3=myset1.intersection(myset2)
# print(myset3)

# Approach 2: using and & symbol
# myset1={'a','b','c',10}
# myset2={10,20,30,'a'}
# myset3=myset1 &myset2
# print(myset3)