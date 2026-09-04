# Fixtures: it is a reusable function. Mot a test function

import pytest

@pytest.fixture
def setup():
     print("Setup Browser")
     return "Chrome"

def test_one(setup):   #Prefferable with python and playwright
     print("This is My Test One")
     print("Browser is:", setup)

def test_two():
     print("This is My Test Two")

def test_three():
     print("This is My Test Three")


# pytest day16\test_demos_fixtures_returns.py -s -v