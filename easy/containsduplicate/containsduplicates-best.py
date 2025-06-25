def checkDup(nums):
    return len(set(nums)) < len(nums)

print("This should return false")
print(checkDup([1,2,3,4]))
print()
print("This should return true")
print(checkDup([1,2,3,4,5,5]))
