from gameoflife import __version__

import gameoflife.main #I want to keep the namespace by trying the below line. 
# from ..src.gameOfLife import main
# unfortunately that does not work. Thus a workaround to keep namespace:

# Workaround to keep namespace

def test_main_module_find():
    assert gameoflife.main.hello_test_integration() == "hello test world"

def test_version():
    assert __version__ == '0.1.0'