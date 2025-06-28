def validAnagram(first, second):
    return sorted(first) == sorted(second)

print("this should return false, we are testing jar and jam")
print(validAnagram("jar", "jam"))
print()
print("this should return true, we are testing racecar and carrace")
print(validAnagram("racecar", "carrace"))
