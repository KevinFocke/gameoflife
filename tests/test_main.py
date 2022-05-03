from gameoflife import __version__

import gameoflife.main  #explicitly maintain namespace information for debugging

def test_main_module_find():
    assert gameoflife.main.hello_test_integration() == "hello test world"

def test_version():
    assert __version__ == '0.1.0'