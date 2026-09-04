import pytest

def test_loginbyemail():
    print("This is login by EMail test")
    assert 1==1

@pytest.mark.skip
def test_loginbyfacebook():
    print("This is login by facebook test")
    assert 1==1

@pytest.mark.skip
def test_loginbyphone():
    print("This is login by phone test")
    assert 1==1

def test_signupbyemail():
    print("This is signup by EMail test")
    assert True==True

@pytest.mark.skip
def test_signupbyfacebook():
    print("This is signup by facebook test")
    assert True==True

@pytest.mark.skip
def test_signupbyphone():
    print("This is signup by phone test")
    assert True==True


# pytest day17\test_skipping.py -s -v