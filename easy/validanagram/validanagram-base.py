def validAnagram(first, second):

    f = []
    s = []

    for letter in first:
        f.append(letter)

    for letter in second:
        s.append(letter)

    print(sorted(f))
    print(sorted(s))

    return print(sorted(f) == sorted(s))


print("this should return false, we are testing jar and jam")
validAnagram('jar', 'jam')
print()
print("this should return true, we are testing racecar and carrace")
validAnagram('racecar', 'carrace')
