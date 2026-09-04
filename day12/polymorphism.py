
#mystring ="Welcome"
# print(len(mystring))
#
# mylist=[10,20,30,40,50]
# print(len(mylist))
#
# mytuple=(1,2,3,4,5)
# print(len(mytuple))
#
# mydic={"id":123, "name":"MLS"}
# print(len(mydic))

# # Example for method overloading(polymorphism)
#
# class Human:
#     def sayHello(self,name=None):
#         if name is not None:
#             print("Hello "+ name)
#         else:
#             print("Hello")
#
# h=Human()
# h.sayHello()
# h.sayHello("MLS")

# Example 2:
class Calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)

cal=Calculation()

cal.add()
cal.add(10,20)
cal.add(100,200,300)