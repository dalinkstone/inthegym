class Solution:
    def __init__(self):
        self._nums: list[int] = []

    def set_nums(self, nums: list[int]):
        self._nums = nums

    def get_nums(self) -> list[int]:
        return self._nums

    def bucket_sort(self, nums: list[int]) -> list[int]:
        return nums


def main():
    print("This is bucket sort and we are passing [2, 3, 4, 1, 6, 5]")
    print("This should return [1, 2, 3, 4, 5, 6]")

    new_solution = Solution()

    new_solution.set_nums([2, 3, 4, 1, 6, 5])

    input_nums = new_solution.get_nums()

    result = new_solution.bucket_sort(input_nums)

    print(f"{result}")


if __name__ == "__main__":
    main()
