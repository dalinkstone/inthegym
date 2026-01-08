class Solution:
    def __init__(self):
        self._nums: list[int] = []

    def set_nums(self, nums: list[int]):
        self._nums = nums

    def get_nums(self) -> list[int]:
        return self._nums

    def bucket_sort(self, nums: list[int]) -> list[int]:
        max_val = max(nums)
        counts = [0] * (max_val + 1)

        for num in nums:
            counts[num] += 1

        i = 0
        for n in range(0, len(counts)):
            while counts[n] > 0:
                nums[i] = n
                i += 1
                counts[n] -= 1

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
