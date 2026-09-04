'''
pre-requisite: install 'pytest-order' plug-in

pip install pytest-order

'''

import pytest
# Approach 1: order tests by positions
#
# @pytest.mark.order(3)
# def test_logout():
#     print("This is logout test")
#
# @pytest.mark.order(2)
# def test_additem():
#     print("This is additem test")
#
# @pytest.mark.order(1)
# def test_login():
#     print("This is login test")
#
#

# Approach 2: Using before, after


# @pytest.mark.order(before="test_checkout")
# def test_additem():
#     print("This is additem test")
#
# @pytest.mark.order(after="test_additem")
# def test_checkout():
#     print("This is checkout test")
#
# @pytest.mark.order(1)
# def test_login():
#     print("This is login test")

# @pytest.mark.order()
# def test_additem():
#     print("This is additem test")
#
# @pytest.mark.order(after="test_additem")
# def test_checkout():
#     print("This is checkout test")
#
# @pytest.mark.order(1)
# def test_login():
#     print("This is login test")


# Approach 3: Using marker string (user defined)

# @pytest.mark.order("first")
# def test_login():
#     print("This is login test")
#
# @pytest.mark.order()
# def test_additem():
#     print("This is additem test")
#
# @pytest.mark.order("last")
# def test_checkout():
#     print("This is checkout test")


@pytest.mark.order()
def test_additem():
    print("This is additem test")

@pytest.mark.order("last")
def test_checkout():
    print("This is checkout test")

@pytest.mark.order("first")
def test_login():
    print("This is login test")

#  pytest day17/test_ordering.py -s -v