import random


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

    def __init__(
        self,
        randomize=0,
        randomize_seed=random.randint(0, 1000000),
        size=[5, 5],
    ):
        self.set_size(size)
        self.randomize_seed = randomize_seed
        random.seed(randomize_seed)  # allow optionally setting seed
        self.state = [
            [0 for col in range(self.size_y)] for row in range(self.size_x)
        ]
        if randomize == 1:
            [
                [random.random(0, 1) for col in range(self.size_y)]
                for row in range(self.size_x)
            ]


a = Board()
# print(a.state)

# print("testprint")
