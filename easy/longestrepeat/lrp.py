def longestRepeat(s: str) -> int:
    res = 0
    l = 0
    charSet = set()

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])

        res = max(res, r - l + 1)

    return res


print("This is longest repeat using a set and two pointers")
print("So we have a string xyzxyz")
print(
    "The longest substring with no duplicate characters of any kind would be of length 3"
)
print("-----------------------------")
print("This test string is xyzxyz and should return 3")
print(longestRepeat("xyzxyz"))
print("-------------------------")
print("This test string is aabbccdac and should return 3")
print(longestRepeat("aabbccdac"))
print("----------------------")
print("This test string is xxxxx and should return 1")
print(longestRepeat("xxxxx"))
