def isPal(string_one: str, string_two: str) -> bool:

    if string_two[::-1] == string_one:
        return True
    else:
        return False

print("---------")
print("Test 1")
print("Gorilla and Monkey, shoudl return False")
print(isPal("gorilla", "monkey"))
print("---------\n")


print("---------")
print("Test 2")
print("Racecar and Racecar, should return True")
print(isPal("racecar", "racecar"))
print("---------\n")

