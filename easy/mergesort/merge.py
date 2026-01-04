class Solution:
    def __init__(self):
        self._nums: list[int] = []

    def set_nums(self, nums: list[int]) -> list[int]:
        self._nums = nums
        return self._nums

    def merge(self, nums: list[int], start: int, middle: int, end: int) -> list[int]:
        left, right = start, middle + 1
        temp: list[int] = []

        while left <= middle and right <= end:
            if self._nums[left] <= self._nums[right]:
                temp.append(self._nums[left])
                left += 1
            else:
                temp.append(self._nums[right])
                right += 1

        while left <= middle:
            temp.append(self._nums[left])
            left += 1

        while right <= end:
            temp.append(self._nums[right])
            right += 1

        for i in range(start, end + 1):
            self._nums[i] = temp[i - start]

    def merge_sort(self, nums: list[int], start: int, end: int) -> list[int]:
        if end - start + 1 <= 1:
            return self._nums

        middle = (start + end) // 2

        self.merge_sort(self._nums, start, middle)
        self.merge_sort(self._nums, middle + 1, end)

        self.merge(self._nums, start, middle, end)

        return self._nums


def main():
    new_solution: Solution = Solution()

    print("This is merge sort, we are passing [2, 3, 4, 1, 6, 5]")
    print("This should return [1, 2, 3, 4, 5, 6]")

    set_array = new_solution.set_nums([2, 3, 4, 1, 6, 5])

    result = new_solution.merge_sort(set_array, 0, len(set_array) - 1)

    print(f"{result}")


if __name__ == "__main__":
    main()
