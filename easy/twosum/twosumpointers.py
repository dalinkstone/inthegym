
def twoSum(numbers: list, target: int) -> list:
    l, r = 0, len(numbers) - 1

    while l < r:
        curSum = numbers[l] + numbers[r]

        if curSum > target:
            r -= 1
        elif curSum < target:
            l += 1
        else:
            return [l + 1, r + 1]
    return

print("This is the first test case\n")
print("Number list: [1, 2, 3, 4, 5] Target: 6\n")
print(twoSum([1, 2, 3, 4, 5], 6))
print("----------------------\n")
print("This is the second test case\n")
print("Number list: [1, 2, 3, 4, 5] Target: 5\n")
print(twoSum([1, 2, 3, 4, 5], 5))
print("-----------------------------")
