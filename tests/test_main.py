import gameoflife  # package
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


def test_init_wrong_size_alphanumeric():
    with pytest.raises(TypeError):
        gameoflife.main.Board(size=["a", 5])


def test_init_wrong_size_length():
    with pytest.raises(ValueError):
        gameoflife.main.Board(size=[5, 5, 5])


def test_init_wrong_randomize_alphanumeric():
    with pytest.raises(TypeError):
        gameoflife.main.Board(randomize_seed="a")


def test_init_randomize_seed(board_fixture_randomized):
    assert board_fixture_randomized.randomize_seed == 10


def test_init_state_ambiguous():
    with pytest.raises(gameoflife.main.customerrors.AmbiguousError):
        gameoflife.main.Board(state=[2, 8], randomize=1)


# def test_dead_board_next_state(board_fixture_dead):
#     """
#     Does the dead board stay dead?
#     Or have we created life out of nothing all of the sudden?
#     """
#     for cell in board_fixture_dead.next_state():
#         assert cell == 0


# count live neighbors
