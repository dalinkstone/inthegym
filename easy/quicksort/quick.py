class Solution:

    def __init__(self):
        self._nums: list[int] = []

    def set_nums(self, nums: list[int]):
        self._nums = nums

    def get_nums(self) -> list[int]:
        return self._nums

    def quick_sort(self, nums: list[int]) -> list[int]:

        return self.get_nums()

def main():

    print("This is quicksort and we are passing the array [2, 3, 4, 1, 6, 5]")
    print("This should return [1, 2, 3, 4, 5, 6]")

    new_solution = Solution()

    input_nums: list[int] = [2, 3, 4, 1, 6, 5]

    new_solution.set_nums(input_nums)

    solution_nums = new_solution.get_nums()

    result = new_solution.quick_sort(solution_nums)

    print(f"{result}")
