import random


class HashSolver:
    def __init__(self):
        self.id = 0

    def hasher(self, key: int) -> int:
        return ((8 * key) + 2) % 7


def main():
    nums: list[int] = [3, 18, 42, 31, 40, 56, 71]

    new_solver = HashSolver()

    for num in nums:
        print(new_solver.hasher(num))


if __name__ == "__main__":
    main()
