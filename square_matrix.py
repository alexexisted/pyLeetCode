from typing import List

def diagonalSum(mat: List[List[int]]) -> int:
    lenght = len(mat[0])
    fin_sum = 0
    for i in range(lenght):
        fin_sum += mat[i][i]
        fin_sum += mat[i][lenght-i-1]
    if lenght % 2 != 0:
        fin_sum -= mat[lenght // 2][lenght // 2]
    return fin_sum

print(diagonalSum([[5]]))