def arraySign(nums: [int]):
    # if 0 in nums:
    #     return 0
    res = 1
    counter = 0

    for i in nums:
        if i < 0:
            counter += 1
        elif i == 0:
            return 0
    if counter % 2 == 0:
        return 1
    else:
        return -1

    # for i in nums:
    #     res *= i
    #
    # if res > 0:
    #     return 1
    # else:
    #     return -1

# print(arraySign([-1,-2,-3,-4,3,2,1]))
print(arraySign([-1, 1, -1, 1, -1]))