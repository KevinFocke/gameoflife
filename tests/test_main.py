from gameoflife import __version__

import gameoflife.main  #explicitly maintain namespace information for debugging

#general testing
def test_main_module_find():
    assert gameoflife.main.module_sanity_check() == 1

def test_version():
    assert __version__ == '0.1.0'


# Test board states

## Board initialized with random values?

