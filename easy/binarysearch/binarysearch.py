def binarySearch(nums, target):
    low = 0
    high = len(nums) - 1
    iterations = 0

    while low <= high:
        mid = (low + high) // 2
        guess = nums[mid]

        if guess == target:
            return mid

        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
        print(f"Count of Iterations: {iterations}\n")
        iterations += 1 
    return None


print("This is an array of numbers 1-100 and a target of 82")
print(binarySearch(list(range(1, 101)), 82))
print()
print("This is an array of numbers 1-1000 and a target of 820")
print(binarySearch(list(range(1, 1001)), 820))
