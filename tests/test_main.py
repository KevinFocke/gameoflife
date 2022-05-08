import gameoflife.main  # explicitly maintain namespace information for debug
from gameoflife import __version__

# Sanity checks


def test_main_module_found():
    assert gameoflife.main.module_sanity_check() == 1


def test_fixture_input_via_conftest(sanity_check_fixture):
    """
    conftest.py is used to supply fixtures accross test files
    """
    assert sanity_check_fixture == "testinput"


def test_multi_assert_single_array(sanity_check_array):
    """Can you do multiple asserts on an array?"""
    for el in sanity_check_array:
        assert el == 1


def test_multi_assert_nested_array(sanity_check_nested_array):
    """Can you do multiple asserts on a nested array"""
    for row in sanity_check_nested_array:
        for el in row:
            assert el == 1


# Test board states


def test_init_board(dead_board_fixture):
    """
    Does the board get initialized?
    """
    assert dead_board_fixture.state  # returns true if object exists


# def test_dead_board_next_state(dead_board_fixture):
#     """
#     Does the dead board stay dead?
#     Or have we created life out of nothing all of the sudden?
#     """
#     for cell in dead_board_fixture.next_state():
#         assert cell == 0


# count live neighbors
