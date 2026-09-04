# creating a tuple

# mytuple=("apple", "banana", "cherry")
# print(mytuple)

# Accessing Tuple items/values/elements
# mytuple=("apple", "banana", "cherry")
# print(mytuple[0])
# print(mytuple[-1])

# count number of times values/elements repeated
# mytuple=("apple", "banana", "cherry",'apple','banana','apple')
# print(mytuple.count("apple")) # 3

# range of indexes
# mytuple = ("Mango", "Apple","Cherry", "Orange", "Kiwi", "Papaya", "Watermelon", "Guava")
# print(mytuple[2:6])
# print(mytuple[-4:-1])

# change values in tuple
# by default tuple won't allow you to change value as tuple is immutable
# but there is a work around
# tuple ----> list ----> tuple
# mytuple=("apple", "banana", "cherry")
# # mytuple[0]="Orange"
# print(mytuple)
# mylist = list(mytuple)
# print("After converting tuple to list: ",mylist)
# mylist[1]="Orange"
# print("After changing value in list: ",mylist)
# mytuple=tuple(mylist)
# print(mytuple)

# retrieve the data from tuple by using looping statement
# mytuple=("apple", "banana", "cherry")
# for i in mytuple:
#     print(i)

# item exist in a tuple(searching for a value in tuple)
# mytuple = ("Mango", "Apple","Cherry", "Orange", "Kiwi", "Papaya", "Watermelon", "Guava")
# print("Cherry" in mytuple) # True
# if "Cherry" in mytuple:
#     print("Exists")
# else:
#     print("Not exists")

# length or count number of values in tuple
# mytuple = ("Mango", "Apple","Cherry", "Orange", "Kiwi", "Papaya", "Watermelon", "Guava")
# print(len(mytuple))
# print(mytuple.count("Apple"))

# adding values is not possible in Tuple as tuple is immutable
# mytuple=("apple", "banana", "cherry")
# mytuple[3]="Orange" # invalid/incorrect

# Copying the tuple
# mytuple=("apple", "banana", "cherry")
# mytuple2=mytuple
# print(mytuple2)

# Removing values from tuple is also not possible
# mytuple=("apple", "banana", "cherry")
# mytuple.remove("apple") # invalid/incorrect

# joining the tuple
# mytuple1 = ("a", "b", "c")
# mytuple2 = (1,2,3)
# mytuple3=mytuple1+mytuple2
# print(mytuple3)
