def twoSum(nums, target):

    numbers = {}

    for i, num in enumerate(nums):
        difference = target - num
        
        if difference in numbers:
            return [numbers[difference], i]
        
        numbers[num] = i

    return

print("This should print [0, 1]")
print(twoSum([3,4,5,6], 7))
print()
print("This should print [0, 2")
print(twoSum([4,5,6], 10))

