import pytest

def test_one():   #Prefferable with python and playwright
    print("This is My Test One")

def test_two():
    print("This is My Test Two")

def test_three():
    print("This is My Test Three")

# class TestClass: #Preferrable for Selenium with python mostly
#     def test_one(self):
#         print("This is My Test One")
#
#     def test_two(self):
#         print("This is My Test Two")
#
#     def test_three(self):
#         print("This is My Test Three")


''' 
To run all the tests in the module
    pytest test_demo.py
    pytest test_demo.py -s
    pytest test_demo.py -s -v

To run specific tests in the module
    pytest test_demo.py::test_one -s -v
    pytest test_demo.py::test_two -s -v
    pytest test_demo.py::test_three -s -v

-s: You can see all print() outputs live in the console while the test runs)
-v: Runs pytest in verbose mode. Shows detailed test execution information)
'''

