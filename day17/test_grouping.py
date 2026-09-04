'''
grouping tests:
---------------
test_LoginByEmail -> sanity, regression
test_LoginByfacebook -> sanity
test_LoginByphone -> Regression
test_signupByEmail -> sanity, regression
test_signupByfacebook   -> Regression
test_signupByphone -> sanity
test_paymentinDollar -> sanity, regression
test_paymentinrupees -> Regression
'''

'''
1) Run only sanity tests: pytest day17\test_grouping.py -v -s -m "sanity"
2) Run only regression tests: pytest day17\test_grouping.py -v -s -m "regression"
3) Run both sanity and regression tests: pytest day17\test_grouping.py -v -s -m "sanity and regression"
4) Run only sanity that not belongs to regression tests: pytest day17\test_grouping.py -v -s -m "sanity" -m "not regression"
5) Run only regression that not belongs to sanity tests: pytest day17\test_grouping.py -v -s -m "regression" -m "not sanity"
'''


import pytest

@pytest.mark.sanity
@pytest.mark.regression
@pytest.mark.skip
def test_loginbyemail():
    print("This is login by EMail test")
    assert 1==1

@pytest.mark.sanity
def test_loginbyfacebook():
    print("This is login by facebook test")
    assert 1==1

@pytest.mark.regression
def test_loginbyphone():
    print("This is login by phone test")
    assert 1==1

@pytest.mark.sanity
@pytest.mark.regression
def test_signupbyemail():
    print("This is signup by EMail test")
    assert True==True


@pytest.mark.regression
def test_signupbyfacebook():
    print("This is signup by facebook test")
    assert True==True

@pytest.mark.sanity
def test_signupbyphone():
    print("This is signup by phone test")
    assert True==True

@pytest.mark.sanity
@pytest.mark.regression
def test_paymentindollar():
    print("This is payment in dollar test")
    assert True==True


@pytest.mark.regression
def test_paymentinrupee():
    print("This is payment in rupee test")
    assert True==True

# pytest day17\test_grouping.py -s -v