from gameoflife import __version__
import gameoflife.main  # explicitly maintain namespace information for debugging

# Sanity checks
def test_main_module_found():
    assert gameoflife.main.module_sanity_check() == 1


def test_version():
    assert __version__ == "0.1.0"


def test_fixture_input_via_conftest(sanity_check_fixture):
    """
    conftest.py is used to supply fixtures accross test files
    """
    assert sanity_check_fixture == "testinput"


# Test board states

# Board initialized with random values?


# count live neighbors
