# Dictionaries are used to store data values in key:value pairs
# for python version prior to 3.7 dictionaries are unordered
# Dictionary items are ordered, changeble (mutable), and do not allow duplicates
# Dictionary items represented in key:value pairs, and can be referred by using key name.
# Key should be allways in ""
# { }

# 1. Creating a dictionary

# Approach 1:
# # mydic = {"Brand":"Ford", "Model":'Aspire',"Year":2024}
# mydic = {
#         "Brand":"Ford",
#         "Model":'Aspire',
#         "Year":2024
#     }
# print(mydic)

# Approach 2: using dict() constructor
# mydic = dict(name="MLS", age=34, country='India')
# print(mydic)

# a key can have multiple values
# mydic = {
#         "Brand":"Ford",
#         "Model":'Aspire',
#         "Year":2024,
#         "Colors": ['Red',"Blue","White"]
#         }
# print(mydic)

# Accessing items/values from dictionary by referring to its key name, inside [] brackets
# Approach 1:
# mydic = {"Brand":"Ford", "Model":'Aspire',"Year":2024}
# print(mydic["Model"])

# Approach 2: using get() method
# mydic = {"Brand":"Ford", "Model":'Aspire',"Year":2024}
# print(mydic.get("Brand"))

# Get keys: keys() method will return a list of keys in dictionary.
# mydic = {
#         "Brand":"Ford",
#         "Model":'Aspire',
#         "Year":2024,
#         "Colors": ['Red',"Blue","White"]
#         }
# keys = mydic.keys()
# print(keys)

# Get values: values() method will return a list of values in dictionary.
# mydic = {
#         "Brand":"Ford",
#         "Model":'Aspire',
#         "Year":2024,
#         "Colors": ['Red',"Blue","White"]
#         }
# value = mydic.values()
# print(value)

# Repeating the keys will replace the value of that key
# mydic = {
#         "Brand":"Ford",
#         "Model":'Aspire',
#         "Year":2024,
#         "Colors": ['Red',"Blue","White"],
#         "Brand":"Honda"
#         }
# print(mydic)

# Get both key and values: items() method will return a list of all keys and values in dictionary.
# mydic = {
#         "Brand":"Ford",
#         "Model":'Aspire',
#         "Year":2024,
#         "Colors": ['Red',"Blue","White"]
#         }
# items = mydic.items()
# print(items) # will return as tuples in list
# print(mydic)

# searching a key in dictionary
# mydic = {
#         "Brand":"Ford",
#         "Model":'Aspire',
#         "Year":2024,
#         "Colors": ['Red',"Blue","White"]
#         }
# if "Model" in mydic:
#     print("Exists")
# else:
#     print("Not exists")

# Adding items to the dictionary
# mydic = {
#         "Brand":"Ford",
#         "Model":'Aspire',
#         "Year":2024
#         }
# mydic["Color"] = "Red"
# print("After adding Key and Value:", mydic)

# Updating dictionary: update()
# mydic = {"Brand":"Ford","Model":'Aspire',"Year":2024}
# mydic["Color"] = "Red"
# print("Before updating", mydic)
# mydic.update({"Year":2026})
# mydic.update({"Color":"Black"})
# print("After updating", mydic)

# Removing items from dictionary
# Approach 1:Using pop()
# mydic = {"Brand":"Ford","Model":'Aspire',"Year":2024, "Color":"Red"}
# mydic.pop("Year")
# print(mydic)

# Approach 2:Using popitem()
# mydic = {"Brand":"Ford","Model":'Aspire',"Year":2024, "Color":"Red"}
# mydic.popitem() # this will delete last inserted item. Prior 3.7 it used to delete random item.
# print(mydic)

# Approach 3:Using del
# mydic = {"Brand":"Ford","Model":'Aspire',"Year":2024, "Color":"Red"}
# del mydic["Model"]
# print(mydic)

# mydic = {"Brand":"Ford","Model":'Aspire',"Year":2024, "Color":"Red"}
# del mydic # deletes entire directory
# print(mydic) # gets name error

# Approach 4: clear() method clears the dictionary
# mydic = {"Brand":"Ford","Model":'Aspire',"Year":2024, "Color":"Red"}
# mydic.clear()
# print(mydic)

# Copying the dictionary
# Approach 1: using copy()
# mydic1 = {"Brand":"Ford","Model":'Aspire',"Year":2024, "Color":"Red"}
# mydic2 = mydic1.copy() # mydic2=mydic1 will have an impact when values in one dic got changed then the same will get updated in second one
#
# print(mydic1)
# print(mydic2)

# Approach 1: using dict()
# mydic1 = {"Brand":"Ford","Model":'Aspire',"Year":2024, "Color":"Red"}
# mydic2=dict (mydic1)
#
# print(mydic1)
# print(mydic2)

# Length of Dictionary
# mydic1 = {"Brand":"Ford","Model":'Aspire',"Year":2024, "Color":"Red"}
# print(len(mydic1))

# Length of Dictionary
# print all keys in dictionary one by one
# mydic1 = {"Brand":"Ford","Model":'Aspire',"Year":2024, "Color":"Red"}
# for x in mydic1:
#     print(x)

# mydic1 = {"Brand":"Ford","Model":'Aspire',"Year":2024, "Color":"Red"}
# for x in mydic1.keys():
#     print(x)

# print all values in dictionary one by one
# mydic1 = {"Brand":"Ford","Model":'Aspire',"Year":2024, "Color":"Red"}
# for x in mydic1:
#     print(mydic1[x])
# for x in mydic1.values():
#     print(x)

# print all keys and values in dictionary one by one
mydic1 = {"Brand":"Ford","Model":'Aspire',"Year":2024, "Color":"Red"}
for x,y in mydic1.items():
    print(x,y)
