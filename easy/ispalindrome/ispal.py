def isPal(word: str) -> bool:

    if word[::-1] == word:
        return True
    else:
        return False

print("---------")
print("Test 1")
print("Monkey, should return False")
print(isPal("monkey"))
print("---------\n")


print("---------")
print("Test 2")
print("Racecar, should return True")
print(isPal("racecar"))
print("---------\n")

