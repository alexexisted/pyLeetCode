from typing import List

def maximumWealth(accounts: List[List[int]]) -> int:
    max_w = 0
    max_w2 = 0
    ind = 0
    while len(accounts) > ind:
        # print(len(accounts[ind]), accounts[ind], ind)
        max_w += sum(accounts[ind])
        if max_w > max_w2:
            max_w2 = max_w
            max_w = 0
            ind += 1
        else:
            max_w = 0
            ind += 1
            continue


    return max_w2


print(maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))