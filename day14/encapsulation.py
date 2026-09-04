# Example 1:

class Student():
    def __init__(self,name):
        self.name=name
        self.__marks=0   # __ will make it a private variable

    # getter method
    def get_marks(self):
        return self.__marks

    # setter method
    def set_marks(self,marks):
        if marks<=100:
            self.__marks=marks
        else:
            print("Invalid marks. marks must be <=100")

# Usage
stu=Student("MLS")
stu.set_marks(90)
print(stu.get_marks())