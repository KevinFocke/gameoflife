import random
import types

import customerrors


def module_sanity_check():

    """
    Can the module be found during testing?
    """
    return 1


class Board:
    def check_size(self, size):
        if len(size) != 2:
            raise ValueError("expected size arg to be [int,int]")
        if not all(isinstance(el, int) for el in size):
            raise TypeError("expected size arg to be [int,int]")

    def __set_size(self, state, size):
        size_new = size
        if state != 0:
            print("setting size based on provided state")
            self.check_state(state)
            x, y = len(state[0]), len(state[1])
            size_new = [x, y]
        self.check_size(size)
        self.size_x, self.size_y = size_new

    def check_randomize_seed(self, randomize_seed):
        if not isinstance(randomize_seed, int):
            raise TypeError

    def __set_randomize_seed(self, randomize_seed):
        self.check_randomize_seed(randomize_seed)
        self.randomize_seed = randomize_seed
        random.seed(self.randomize_seed)

    def check_randomize(self, randomize):
        if randomize not in [0, 1]:
            raise ValueError("randomize value incorrect; expected 0 or 1")

    def __set_randomize(self, randomize):
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
                raise ValueError(
                    "expected list with multiple values per dimension"
                )

    def _initialize_cells(self, action_per_cell):
        """
        Method intended for initialization.
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
        yields: [base_cell_state, x_pos, y_pos]"""
        for row in range(self.size_x):
            for col in range(self.size_y):
                yield [self.state[row][col], row, col]
                # iterator is a generator

    def __set_state(self, state=0, randomize=0):
        self.check_state_ambiguity(
            state, randomize
        )  # avoid overwriting provided state
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
                    self._check_pos_in_board(
                        x_pos + row_offset, y_pos + col_offset
                    )
                except ValueError:
                    continue
                # check cell state
                if self.state[x_pos + row_offset][y_pos + col_offset] == 1:
                    neighbour_count += 1
        return neighbour_count

    def _decide_and_set(self, base_cell_state, neighbour_count, x_pos, y_pos):
        """Decide cell state & set"""
        if base_cell_state == 1 and neighbour_count <= 1:
            self.state[x_pos][y_pos] = 0  # underpopulation
            return 0
        if base_cell_state == 1 and 2 >= neighbour_count <= 3:
            return 0  # no need to set, already alive
        if base_cell_state == 1 and neighbour_count > 3:
            self.state[x_pos][y_pos] = 0  # overpopulation
            return 0
        if base_cell_state == 0 and neighbour_count == 3:
            self.state[x_pos][y_pos] = 1  # reproduction
            return 0

    def next_step(self):
        """Calculates neighbours, updates state & Increments the step"""

        # For every cell

        # Check neighbour count
        # Decide cell state
        # Change cell state
        for cell in self:
            base_cell_state, x_pos, y_pos = cell[0], cell[1], cell[2]
            cell_neighbours = self._count_neighbours(x_pos=x_pos, y_pos=y_pos)
            self._decide_and_set(
                base_cell_state, cell_neighbours, x_pos, y_pos
            )

    def __init__(
        self,
        state=0,
        randomize=0,
        randomize_seed=random.randint(0, 1000000),
        size=[5, 5],
    ):
        self.__set_size(state, size)
        self.__set_randomize_seed(randomize_seed)
        self.__set_randomize(randomize)
        self.__set_state(state, randomize)
        self.step = 0  # step starts at 0


# cross-platform display emulation
# TODO: Generate big fixture for performance testing
