def validAnagram(first, second):

    if len(first) != len(second):
        return False

    countFirst, countSecond = {}, {}

    for i in range(len(first)):
        countFirst[first[i]] = 1 + countFirst.get(first[i], 0)
        countSecond[second[i]] = 1 + countSecond.get(second[i], 0)

    return countFirst == countSecond


print("this should be false, testing jar and jam")
print(validAnagram("jar", "jam"))
print()
print("this should be true, testing racecar and carrace")
print(validAnagram("racecar", "carrace"))
