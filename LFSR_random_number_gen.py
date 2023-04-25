import time

# very basic random number generator. Generates random values lying in a certain region depending on the time.


class Randomness:
    def __init__(self, start=1, end=65536):
        self.start = start
        self.end = end

    def random(self=True):
        root = int(time.time()//1)
        for i in range(16):
            new = (root ^ (root >> 1)) & 1
            root = (root >> 1) | (new << 30)
        print(root)


if __name__ == "__main__":
    Randomness.random()
