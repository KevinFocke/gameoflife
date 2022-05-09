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

    def set_size(self, size):
        self.check_size(size)
        self.size_x, self.size_y = size

    def check_randomize_seed(self, randomize_seed):
        if not isinstance(randomize_seed, int):
            raise TypeError

    def set_randomize_seed(self, randomize_seed):
        self.check_randomize_seed(randomize_seed)
        self.randomize_seed = randomize_seed
        random.seed(self.randomize_seed)

    def set_randomize(self, randomize, randomize_seed):
        self.check_randomize(randomize_seed)
        random.seed(randomize_seed)  # set random seed for determinism
        self.randomize_seed = randomize_seed
        if randomize == 0:
            return False  # state not randomized

    def check_state_ambiguity(self, state, randomize):
        """Avoid randomizing a given state"""
        if state != 0 and randomize == 1:
            raise customerrors.AmbiguousError

    def set_state(self, state=0, randomize=0):
        self.check_state_ambiguity(state, randomize)
        #

    def __init__(
        self,
        state=0,
        randomize=0,
        randomize_seed=random.randint(0, 1000000),
        size=[5, 5],
    ):
        self.set_size(size)
        self.set_randomize_seed(randomize_seed)
        self.set_state(state, randomize)
        self.state = [
            [0 for col in range(self.size_y)] for row in range(self.size_x)
        ]
        if randomize == 1:
            [
                [random.randint(0, 1) for col in range(self.size_y)]
                for row in range(self.size_x)
            ]


a = Board()
# print(a.state)

# print("testprint")
