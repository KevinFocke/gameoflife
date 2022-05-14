import copy
import random
import types
from functools import wraps

import click

import customerrors


def module_sanity_check(*args, **kwargs):

    """
    Can the module be found during testing?
    """
    return 1


class Board:
    def check_size(self, size):
        """Check if size parameter is formatted correctly"""
        if len(size) != 2:
            raise ValueError("expected size arg to be [int,int]")
        if not all(isinstance(el, int) for el in size):
            raise TypeError("expected size arg to be [int,int]")

    def __set_size(self, state, size):
        """Set the board size. If state is provided, set based on state."""
        size_new = size
        if state != 0:
            print("Setting size based on provided state. Size parameter is ignored.")
            self.check_state(state)
            x, y = len(state[0]), len(state[1])
            size_new = [x, y]
        self.check_size(size)
        self.size_x, self.size_y = size_new

    def check_randomize_seed(self, randomize_seed):
        """Check if randomize_seed is formatted correctly"""
        if not isinstance(randomize_seed, int):
            raise TypeError

    def __set_randomize_seed(self, randomize_seed):
        """Set the randomize_seed"""
        self.check_randomize_seed(randomize_seed)
        self.randomize_seed = randomize_seed
        random.seed(self.randomize_seed)

    def check_randomize(self, randomize):
        """Check if randomize is formatted correctly."""
        if randomize not in [0, 1]:
            raise ValueError("randomize value incorrect; expected 0 or 1")

    def __set_randomize(self, randomize):
        """Set the randomize"""
        self.check_randomize(randomize)
        self.randomize = randomize

    def check_state_ambiguity(self, state, randomize):
        """Avoid randomizing a given state"""
        if state != 0 and randomize == 1:
            raise customerrors.AmbiguousError(
                "state is provided, yet randomize is requested."
            )

    def __generate_state_value(self):
        """If randomize flag is set, return a random lambda function
        else return 0"""
        if self.randomize == 1:
            return lambda: random.randint(0, 1)
        else:
            return 0

    def check_state(self, state):
        """
        checks if state is expected format:
        eg. [[1,0],[0,1]]
        """
        accepted_values = [0, 1]
        expected_format = "[[1,0],[0,1]]"
        if not all(isinstance(el, list) for el in state):
            raise TypeError("expected list of lists format:" + expected_format)
        for dim in state:
            # check that each element is 0 or 1
            for el in dim:
                if el not in accepted_values:
                    raise ValueError("Expected state values between 0 and 1")
            # check each dimension is >= 1
            if not len(dim) > 1:
                raise ValueError("expected list with multiple values per dimension")

    def _initialize_cells(self, action_per_cell):
        """
        Method intended for initialization of state.
        If action is a lambda it will invoke the function.
        Else use a value.

        Why use lambda function?

        To generate a fresh value with every cell.

        Otherwise the action would be evaluated only once.
        """

        # Check if the action is a lambda function
        # Why use isinstance AND namecheck?
        # Because isinstance(obj,LambdaType) is true for any function
        # __name__ = "<lambda>" ensures it is an actual lambda
        if (
            isinstance(action_per_cell, types.LambdaType)
            and action_per_cell.__name__ == "<lambda>"
        ):
            invoke_lambda = 1
        else:
            invoke_lambda = 0

        return [
            [
                action_per_cell() if invoke_lambda == 1 else action_per_cell
                for col in range(self.size_y)
            ]
            for row in range(self.size_x)
        ]

    def __iter__(self):
        """Iterate over board
        yields: [cell_state, x_pos, y_pos]"""
        for row in range(self.size_x):
            for col in range(self.size_y):
                yield [self.state[row][col], row, col]
                # iterator is a generator

    def __set_state(self, state=0, randomize=0):
        """Set the board state. If randomize flag is set, generate state."""
        self.check_state_ambiguity(
            state, randomize
        )  # avoid overwriting provided state`:a`
        random.seed(self.randomize_seed)  # ensure determinism

        # Set state to provided
        if state != 0:
            self.check_state(state)
            self.state = state

        # Generate random state
        else:
            self.state = self._initialize_cells(self.__generate_state_value())

    def _check_pos_in_board(self, x_pos, y_pos):
        """Does the cell exist within the board?Why < self.size_x?
        Becuase size_x is one-indexed"""
        if not ((0 <= x_pos < self.size_x) and (0 <= y_pos < self.size_y)):
            raise (ValueError)

    def _count_neighbours(self, x_pos, y_pos):
        """Counts the cell's neighbours.
        Returns the value (zero-indexed)
        """
        # Do the arguments exist on the board?
        # size_x and size_y are one-indexed

        # Does the board position exist?
        self._check_pos_in_board(x_pos, y_pos)

        # Count neighbours by offsetting base cell
        neighbour_count = 0

        for row_offset in range(-1, 2):
            for col_offset in range(-1, 2):
                # skip base cell
                if row_offset == 0 and col_offset == 0:
                    continue
                # does the offset cell exist?
                try:
                    self._check_pos_in_board(x_pos + row_offset, y_pos + col_offset)
                except ValueError:
                    continue
                # check cell state
                if self.state[x_pos + row_offset][y_pos + col_offset] == 1:
                    neighbour_count += 1
        return neighbour_count

    def _decide_and_set_proposed(self, cell_state, neighbour_count, x_pos, y_pos):
        """Decide cell state & set proposed state."""
        if cell_state == 1 and neighbour_count <= 1:
            self.proposed_state[x_pos][y_pos] = 0  # underpopulation
            return 0
        if cell_state == 1 and 2 >= neighbour_count <= 3:
            return 0  # no need to set, already alive
        if cell_state == 1 and neighbour_count > 3:
            self.proposed_state[x_pos][y_pos] = 0  # overpopulation
            return 0
        if cell_state == 0 and neighbour_count == 3:
            self.proposed_state[x_pos][y_pos] = 1  # reproduction
            return 0

    def pretty_print(self):
        """Pretty prints the board state + step
        If descriptors = 0, only print state"""
        print(f"Step {self.step} state:")
        for row in self.state:
            print(f"{row}")

    def _proposed_state_to_current(func):
        """
        Updates state once all cells are evaluated."""

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            self.pretty_print()  # state before
            self.proposed_state = copy.deepcopy(self.state)
            func(self, *args, **kwargs)
            self.state = self.proposed_state
            self.step += 1
            self.pretty_print()  # state after

        return wrapper

    @_proposed_state_to_current
    def _next_board_state(self):
        """Calculates neighbours, updates state & Increments the step.
        Needs _proposed_state_to_current wrapper
        to ensure each cell is evaluated in the same state

        Note: There is coupling between _next_board_state(),_decide_and_set_proposed()
        ,and _proposed_state_to_current().
        However, in my opinion it's justified in this case to make the logic explicit.
        The proposed state should only be committed
        when the current state is fully evaluated.
        Thus the evaluation should read from self.state,
        and write to self.proposed_state"""

        # For every cell:
        # Check neighbour count
        # Decide cell state
        # Change cell state
        for cell in self:
            cell_state, x_pos, y_pos = cell[0], cell[1], cell[2]
            cell_neighbours = self._count_neighbours(x_pos=x_pos, y_pos=y_pos)
            self._decide_and_set_proposed(cell_state, cell_neighbours, x_pos, y_pos)

    def check_next_step(self, steps):
        if not isinstance(steps, int):
            raise TypeError("Provided non-numeric input")
        if steps < 0:
            raise ValueError("Negative number")

    def next_step(self, steps=1):
        """Calculates and sets next board state"""
        self.check_next_step(steps)
        for step in range(steps):
            self._next_board_state()

    def __init__(
        self,
        state=0,
        randomize=0,
        randomize_seed=random.randint(0, 1000000),
        size=[5, 5],
    ):
        """Runs when object is initialized"""
        self.__set_size(state, size)
        self.__set_randomize_seed(randomize_seed)
        self.__set_randomize(randomize)
        self.__set_state(state, randomize)
        self.step = 0  # step starts at 0


# Command line interface
@click.command()
@click.option("--randomize", default=0, help="Randomize the board")
@click.option(
    "--randomize_seed",
    default=random.randint(0, 1000000),
    help="Set randomization seed for deterministic randomization",
)
@click.option(
    "--size_x",
    default=5,
    help="Explicitly set y dimension. \n Flag gets ignored if state is also provided.",
)
@click.option(
    "--size_y",
    default=5,
    help="Explicitly set x dimension. \n Flag gets ignored if state is also provided.",
)
@click.option("--steps", default=1, help="Amount of steps to take")
def program_runner(randomize, randomize_seed, size_x, size_y, steps):
    size = [size_x, size_y]
    myboard = Board(randomize=randomize, randomize_seed=randomize_seed, size=size)
    myboard.next_step(steps=steps)


if __name__ == "__main__":
    program_runner()

# Typical use case:

# myBoard = Board(randomize=1, size=[10, 10])
# myBoard.next_step(5)
