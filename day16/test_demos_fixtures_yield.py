# Fixtures: it is a reusable function. Mot a test function

import pytest

@pytest.fixture
def setup():               #Entry of every test function
     print("Setup Browser")
     yield                 #Exit of every test function
     print("close browser")

def test_one(setup):   #Prefferable with python and playwright
     print("This is My Test One")

def test_two(setup):
     print("This is My Test Two")

def test_three(setup):
     print("This is My Test Three")


# pytest day16\test_demos_fixtures_yield.py -s -v