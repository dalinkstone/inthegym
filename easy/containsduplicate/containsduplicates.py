def checkDup(nums):

    checker = set()

    for num in nums:
        if num in checker:
            return True
        checker.add(num)
    return False

print("This should return false")
print(checkDup([1,2,3,4]))
print()
print("This should return true")
print(checkDup([1,2,3,4,5,5]))
