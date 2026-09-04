# Fixtures: it is a reusable function. Mot a test function
# scope: "function" fixture will be called before every test function executes
# scope: "module" fixture will be called only once before test function executes
# scope: "class" fixture will be called only once before the class
# scope: "session" fixture will be called only once for session

#module --> class --> methods
#module --> function

import pytest

@pytest.fixture
def setup(scope="module"):
    print("Setup Browser")

def test_one(setup):   #Prefferable with python and playwright
     print("This is My Test One")

def test_two():
     print("This is My Test Two")

def test_three(setup):
     print("This is My Test Three")


# pytest day16\test_demos_fixtures.py -s -v