from typing import List

def moveZeroes(nums: List[int]):
    left = []
    right = []
    for i in nums:
        if i == 0:
            right.append(i)

        else:
            left.append(i)

    nums.clear()
    ind = 0
    for j in left:
        nums.append(j)

    for k in right:
        nums.append(k)

    return nums


print(moveZeroes([0, 0, 1]))