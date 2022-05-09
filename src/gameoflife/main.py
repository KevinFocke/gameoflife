import random

import customerrors


def module_sanity_check():

    """
    Can the module be found during testing?
    """
    return 1

    # if __name__ == "__main__":


class Board:
    def check_size(self, size):
        if len(size) != 2:
            raise ValueError
        if not all(isinstance(el, int) for el in size):
            raise TypeError

    def __set_size(self, size):
        self.check_size(size)
        self.size_x, self.size_y = size

    def check_randomize_seed(self, randomize_seed):
        if not isinstance(randomize_seed, int):
            raise TypeError

    def __set_randomize_seed(self, randomize_seed):
        self.check_randomize_seed(randomize_seed)
        self.randomize_seed = randomize_seed
        random.seed(self.randomize_seed)

    def check_randomize(self, randomize):
        if randomize not in [0, 1]:
            raise ValueError

    def __set_randomize(self, randomize):
        self.check_randomize(randomize)
        self.randomize = randomize

    def check_state_ambiguity(self, state, randomize):
        """Avoid randomizing a given state"""
        if state != 0 and randomize == 1:
            raise customerrors.AmbiguousError

    def __generate_state_value(self):
        if self.randomize == 1:
            return random.randint(0, 1)
        else:
            return 0

    def __set_state(self, state=0, randomize=0):
        self.check_state_ambiguity(state, randomize)
        random.seed(self.randomize_seed)  # ensure determinism

        # TODO: check provided state;
        # does it match dimensions?
        # are all cells integers?
        # TODO: create provided state
        if state != 0:
            pass

        # Generate state
        else:
            self.state = [
                [self.__generate_state_value() for col in range(self.size_y)]
                for row in range(self.size_x)
            ]

    def __init__(
        self,
        state=0,
        randomize=0,
        randomize_seed=random.randint(0, 1000000),
        size=[5, 5],
    ):
        self.__set_size(size)
        self.__set_randomize_seed(randomize_seed)
        self.__set_randomize(randomize)
        self.__set_state(state, randomize)
        print("hi")


# a = Board(randomize_seed=10, randomize=1
# TODO: Generate big fixture for performance testing

# print(a.state)

# print("testprint")
