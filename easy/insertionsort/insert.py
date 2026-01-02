class Solution:
    def __init__(self):
        self._nums: list[int] = [2, 3, 4, 1, 6, 5]

    def get_nums(self):
        return self._nums

    def sort(self) -> list[int]:
        sort_nums = self.get_nums()
        for i in range(1, len(sort_nums)):
            j = i - 1
            while j >= 0 and sort_nums[j + 1] < sort_nums[j]:
                temp = sort_nums[j + 1]
                sort_nums[j + 1] = sort_nums[j]
                sort_nums[j] = temp
                j -= 1
        return sort_nums


def main():
    insert_solution = Solution()

    result = insert_solution.sort()

    print("This is insertion sort and we are using the list[int] of [2, 3, 4, 1, 6, 5]")
    print("\nThis should return [1, 2, 3, 4, 5, 6]")
    print(f"{result}")


if __name__ == "__main__":
    main()
