import random
import sys


def module_sanity_check():

    """
    Can the module be found during testing?
    """
    return 1

    # if __name__ == "__main__":


class Board:
    def __init__(
        self,
        randomize=0,
        randomize_seed=random.randint(0, 1000000),
        size=[5, 5],
    ):
        # size 2-dimensional?
        self.init_args = locals()  # store called arguments for debugging
        if self.check_size(*size) == 1:
            sys.exit("error in size argument")
        x, y = size
        self.randomize_seed = randomize_seed
        random.seed(randomize_seed)  # allow optionally setting seed
        self.state = [[0 for col in range(y)] for row in range(x)]
        if randomize == 1:
            [[random.random(0, 1) for col in range(y)] for row in range(x)]

    def check_size(*size):
        size = size[1:]  # do not need board object
        if len(size) != 2 or not any(isinstance(el, int) for el in size):
            return 1


a = Board()
# print(a.state)

# print("testprint")
