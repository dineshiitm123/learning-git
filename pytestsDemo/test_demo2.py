import pytest

@pytest.mark.skip
def test_program():
    msg="Hello"
    assert msg == "hi" , "test failed"

@pytest.mark.smoke
def test_greet():
    print("Good Morning")
    
