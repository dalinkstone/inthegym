def checkDups(nums):

    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print("This should return false")
print(checkDups([1,2,3,4]))
print()
print("This should return true")
print(checkDups([1,2,3,4,5,5]))

