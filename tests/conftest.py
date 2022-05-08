import gameoflife.main  # explicitly maintain namespace information for debug
import pytest

"""
Single source of truth for fixtures across tests
"""

# Scopes of pytest fixtures decide how often they are run.
# Syntax: @pytest.fixture(scope="function")
# Unique polymorphism: You can call the class directly; it returns an object!
# The default scope of a fixture is function; this means:
# The fixture is a wrapper; setup before, teardown after.
# Other possible fixtures are: session, class, module
# You can also make a fixture apply to every test with autouse
# Syntax: @pytest.fixture(autouse=True)


@pytest.fixture
def sanity_check_fixture():
    return "testinput"


@pytest.fixture
def sanity_check_array():
    return [1, 1, 1, 1, 1]


@pytest.fixture
def sanity_check_nested_array():
    return [[1, 1], [1], [1, 1, 1]]


@pytest.fixture
def random_board_fixture():
    return gameoflife.main.Board(randomize=1, randomize_seed=10)


@pytest.fixture
def dead_board_fixture():
    return gameoflife.main.Board(randomize=0)
