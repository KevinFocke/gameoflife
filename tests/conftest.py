import pytest

""" 
Single source of truth for fixtures across tests
"""


@pytest.fixture
def sanity_check_fixture():
    return "testinput"
