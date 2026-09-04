# Example 1: creating a class along with object

# class Myclass:
#     def myfun(self):   # self defines a class
#         pass
#
#     def display(self,name):
#         print(name)
#
# mc1=Myclass()   # mc1 is an object that acquires all methods of the class defined
# mc1.myfun()
# mc1.display("MLS")
#
# mc2=Myclass()
# mc2.myfun()
# mc2.display("Ganesh")

# Example 2: Instance method(discussed in Ex 1:) vs Static method
# self inside a static class is just a parameter and doesn't refer the object
# class Myclass:
#     def m1(self):
#         print("This is instance method...")
#
#     @staticmethod
#     def m2(self,num):
#         print(num)
#
# # mc=Myclass()
# # mc.m1()   # instance method
# # mc.m2(10,20)
#
# Myclass.m1(10) # invalid
# Myclass.m2(1,2) # static methods can be accessed directly from the class

# Example 3: define variables inside the class (class/instance variables)
# class Myclass:
#     a,b = 10,20 # class variables
#     def add(self):
#         # print(a+b) # invalid
#         print(self.a+self.b)
#     def mul(self):
#         print(self.a*self.b)
#
# mc=Myclass()
# mc.add()
# mc.mul()

# Example 4: Local variables, Global variables & class variables

# i,j = 15,25 # global variables
#
# class Myclass:
#     a,b = 10,20 # class variables
#
#     def add(self,x,y):
#         print(x+y) # local variables
#         print(self.a+self.b) # class variables
#         print(i+j) # global variables
#
# mc=Myclass()
# mc.add(100,200)

# Example 5: Local variables, Global variables & class variables (names of all variables are same)

# a,b = 15,25 # global variables
#
# class Myclass:
#     a,b = 10,20 # class variables
#
#     def add(self,a,b):
#         print(a+b) # local variables
#         print(self.a+self.b) # class variables
#         print(globals()['a']+globals()['b']) # global variables
#
#
# mc=Myclass()
# mc.add(100,200)

# Example 6: Class with constructor
# __init__(self) : constructor
# constructor is used to initialize the data
# constructor is automatically invoked when object is created

# class Myclass():
#     def __init__(self):
#         print("This is a Constructor")
#     def m1(self):
#         print("Hello...")
#     def m2(self,x,y):
#         return x+y
# mc=Myclass()
#
# mc.m1()
# print(mc.m2(2,4))

# Example 7: Constructor with parameters

# class Myclass():
#     name = "MLS" # class variable
#
#     def __init__(self,name):
#         print(name) # Ganesh
#         print(self.name) # MLS
#
# mc = Myclass("Ganesh")

# Example 8: A class with constructor and method

class Emp:
    def __init__(self,eid,ename,sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal
    def display(self):
        print(self.eid,self.ename,self.sal)

e1=Emp(101,"MLS",1800000)
e1.display()

e2=Emp(102,"Ganesh",1600000)
e2.display()
