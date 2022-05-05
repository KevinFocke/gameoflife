from gameoflife import __version__
import pytest
import gameoflife.main  #explicitly maintain namespace information for debugging

#Sanity checks
def test_main_module_find():
    assert gameoflife.main.module_sanity_check() == 1

def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture #fixture supplies test input data
def test_fixture_input():
    """
    Does the pytest fixture work?
    """
    return "hello"

def test_fixture_input_working(test_fixture_input):
    assert test_fixture_input == "hello"

# Test board states



# Board initialized with random values?



# count live neighbors
