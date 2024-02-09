from typing import List
def canMakeArithmeticProgression(arr: List[int]) -> bool:
    arr2 = sorted(arr)
    counter1 = arr2[1] - arr2[0]
    counter2 = 0
    ind = 0
    ind2 = 1
    if len(arr2) == 2:
        return True

    while len(arr2) > ind2:
        counter2 = arr2[ind2] - arr2[ind]
        if counter1 != counter2:
            return False
        else:
            ind += 1
            ind2 += 1
    return True

print(canMakeArithmeticProgression([3, 5, 1]))



