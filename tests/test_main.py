import gameoflife.main  # explicitly maintain namespace information for debug
import pytest

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


# Test board

# __init__


def test_init_board(board_fixture_dead):
    """
    Does the board get initialized?
    """
    assert board_fixture_dead.state  # returns true if object exists


@pytest.mark.xfail(raises=TypeError)
def test_init_wrong_size_alphanumeric(board_fixture_wrong_size_alphanumeric):
    pass


@pytest.mark.xfail(raises=ValueError)
def test_init_wrong_size_len(board_fixture_wrong_size_len):
    pass


# def test_dead_board_next_state(board_fixture_dead):
#     """
#     Does the dead board stay dead?
#     Or have we created life out of nothing all of the sudden?
#     """
#     for cell in board_fixture_dead.next_state():
#         assert cell == 0


# count live neighbors
