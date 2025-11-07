def rain(height: list) -> int:
    if not height:
        return 0

    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0

    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]

    return res


print("This is rain water capture using two pointers")
print(
    "We pass a one dimensional array of integers that represent the height of a horizontal plane at a given index location to determine how much rain water can we hold if the heights on both sides allow it"
)
print(
    "So if we are on index 3 and index 2 has a height of one, index 3 has a height of 0, and index 4 has a height of one, this means that we can hold exactly 1 rain water in index 3"
)
print("---------------------------------------")
print(
    "This first test case we pass a one dimensional array of [0,2,0,3,1,0,1,3,2,1]")
print("We should get an output of 9")
print(rain([0, 2, 0, 3, 1, 0, 1, 3, 2, 1]))
