# Example 1:

# class A:
#     def m1(self):
#         print("This is m1 from class A")
#
# class B(A):           # inheriting Class A in Class B
#     def m2(self):
#         print("This is m2 from class B")
#
# bobj=B()
# bobj.m1()
# bobj.m2()

# Example 2: Single inheritance

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=100,200
#     def m2(self):
#         print(self.a - self.b)
#
# bobj=B()
# bobj.m1()
# bobj.m2()

# Example 3: Multilevel inheritance

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=100,200
#     def m2(self):
#         print(self.a - self.b)
#
# class C(B):
#     i,j=5,2
#     def m3(self):
#         print(self.i * self.j)
#
#
# cobj=C()
# cobj.m1()
# cobj.m2()
# cobj.m3()

# Example 4: Hierarchical inheritance

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=100,200
#     def m2(self):
#         print(self.a - self.b)
#
# class C(A):
#     i,j=5,2
#     def m3(self):
#         print(self.i * self.j)
#
#
# cobj=C()
# bobj=B()
# bobj.m1()
# bobj.m2()
# cobj.m1()
# cobj.m3()

# Example 5: Multiple inheritance

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B:
#     a,b=100,200
#     def m2(self):
#         print(self.a - self.b)
#
# class C(A,B):
#     i,j=5,2
#     def m3(self):
#         print(self.i * self.j)
#
#
# cobj=C()
# cobj.m1()
# cobj.m2()
# cobj.m3()

## Example 6: calling parent class method using child class

# class A():
#     def m1(self):
#         print("This is m1 from class A")
#
# class B(A):
#     def m1(self):
#         print("This is m1 from class B")
#         super().m1() # will invoke immediate parent class method
#
# bobj=B()
# bobj.m1()

# # Example 7: calling parent class variables using child class
# class A:
#     a,b = 10,20
#
# class B(A):
#     i,j=100,200
#
#     def m1(self,x,y):
#         print(x+y)  # local variables
#         print(self.i+self.j) # B class variables
#         print(self.a + self.b) # A class variables
#
# bobj=B()
# bobj.m1(1000,2000)

# # Example 8: overriding variables
# class Parent:
#     name="Scott"
#
# class Child(Parent):
#     name="John"  # overrided variable
#     def m(self):
#         print(super().name)
# cobj=Child()
# print(cobj.name) # John
# cobj.m()

# Example 9: Overriding methods

class Bank():
    def rateOfInterest(self):
        return 0

class XBank(Bank):
    def rateOfInterest(self):
        return 10.5

class YBank(Bank):
    def rateOfInterest(self):
        return 12.5

x=XBank()
print(x.rateOfInterest()) # 10.5

y=YBank()
print(y.rateOfInterest()) # 12.5