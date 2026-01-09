class Solution:

    def __init__(self):
        self.__nums: list[int] = []

    def set_nums(self, nums) -> None:
        self.__nums = nums

    def get_nums(self) -> list[int]:
        return self.__nums

    def prefix_max(self, nums: list[int], i: int) -> int:
        if i > 0:
            j = self.prefix_max(nums, i - 1)

            if nums[i] < nums[j]:
                return j

        return i

    def selection_sort(self, nums: list[int], i: int) -> list[int]:
        
        if i > 0:
            j = self.prefix_max(nums, i)

            nums[i], nums[j] = nums[j], nums[i]

            self.selection_sort(nums, i - 1)

        return nums


    
def main():
    print("This is selection sort and we are passing [8, 2, 4, 9, 3]")

    input_nums: list[int] = [8, 2, 4, 9, 3]

    new_solution = Solution()

    result = new_solution.selection_sort(input_nums, len(input_nums) - 1)

    print(f"This is the result {result}")


if __name__ == "__main__":
    main()
