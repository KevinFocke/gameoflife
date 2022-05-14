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


def test_init_randomize_seed_determinism(board_fixture_randomized):
    """Does the random seed produce the same result?"""
    assert board_fixture_randomized.state == [
        [0, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 1, 0, 1, 1],
        [1, 1, 1, 1, 0],
    ]


def test_init_randomize_not_0_or_1():
    with pytest.raises(ValueError):
        gameoflife.main.Board(randomize=2)


def test_init_state_ambiguous():
    with pytest.raises(gameoflife.main.customerrors.AmbiguousError):
        gameoflife.main.Board(state=[[0, 1], [0, 0]], randomize=1)


def test_init_state_dimensions_incorrect_type():
    with pytest.raises(TypeError):
        gameoflife.main.Board(state=[0, 1])


def test_init_state_incorrect_dimension_length():
    with pytest.raises(ValueError):
        gameoflife.main.Board(state=[[0], [1]])


def test_init_state_incorrect_values():
    with pytest.raises(ValueError):
        gameoflife.main.Board(state=[[0, 1], [1, 2]])


def test_init_state_set(board_fixture_state_4_by_4):
    assert board_fixture_state_4_by_4.state == [[0, 1, 1, 1], [1, 1, 1, 0]]


def test_init_state_detect_dimension_mismatch(
    board_fixture_mismatch_state_size,
):
    assert board_fixture_mismatch_state_size.size_x == 3
    assert board_fixture_mismatch_state_size.size_y == 4


# Calculate next step


def test_check_next_step_incorrect_input_alphanumeric():
    with pytest.raises(TypeError):
        board = gameoflife.main.Board(randomize=1, randomize_seed=5)
        board.check_next_step("a")


def test_next_step_incorrect_input_alphanumeric():
    with pytest.raises(TypeError):
        board = gameoflife.main.Board(randomize=1, randomize_seed=5)
        board.next_step("a")


def test_triangle__next_board_state():
    triangle_board = gameoflife.main.Board(
        state=[
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
    triangle_board._next_board_state()
    assert triangle_board.state == [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]


def test_triangle_next_twosteps():
    triangle_board = gameoflife.main.Board(
        state=[
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
    triangle_board.next_step(2)
    assert triangle_board.state == [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]


def test_triangle_board_count_neighbours():
    triangle_board = gameoflife.main.Board(
        state=[
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
    assert triangle_board._count_neighbours(3, 2) == 2


def test_count_neighbours_edge():
    edge_board = gameoflife.main.Board(
        state=[
            [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
    assert edge_board._count_neighbours(0, 0) == 2


def test_count_neighbours_pos_out_of_board_neg_x_pos():
    with pytest.raises(ValueError):
        triangle_board = gameoflife.main.Board(
            state=[
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
        triangle_board._count_neighbours(-1, 2)


def test_count_neighbours_pos_out_of_board_x_pos_off_by_one():
    with pytest.raises(ValueError):
        triangle_board = gameoflife.main.Board(
            state=[
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
        triangle_board._count_neighbours(5, 2)


def test_count_neighbours_pos_out_of_board_neg_y_pos():
    with pytest.raises(ValueError):
        triangle_board = gameoflife.main.Board(
            state=[
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
        triangle_board._count_neighbours(2, -1)


def test_count_neighbours_pos_out_of_board_y_pos_off_by_one():
    with pytest.raises(ValueError):
        triangle_board = gameoflife.main.Board(
            state=[
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
        triangle_board._count_neighbours(2, 5)


def test_single_cell__next_board_state():
    single_cell_board = gameoflife.main.Board(
        state=[
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
    single_cell_board._next_board_state()
    assert single_cell_board.state == [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]


def test_reproduction__next_board_state():
    single_cell_board = gameoflife.main.Board(
        state=[
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0],
        ]
    )
    single_cell_board._next_board_state()
    assert single_cell_board.state == [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]


def test_dead_board_next_state(board_fixture_dead):
    board_fixture_dead._next_board_state()
    assert board_fixture_dead.state == [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]


def test_board_iterator():
    custom_board = gameoflife.main.Board(
        state=[
            [0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0],
        ]
    )
    iteration_list = []
    for cell in custom_board:
        iteration_list.append(cell[0])

    # black auto formats like this. Yikes.
    assert iteration_list == [
        0,
        0,
        1,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        1,
        1,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
    ]


# count live neighbors
