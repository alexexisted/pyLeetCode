from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    cols = len(matrix[0]) #4
    lines = len(matrix) #3
    top = 0
    bottom = lines - 1
    left = 0
    right = cols - 1
    direction = 'right'
    res = []
    while top <= bottom and left <= right:
        if direction == 'right':
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            direction = 'down'

        elif direction == 'down':
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            direction = 'left'

        elif direction == 'left':
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            direction = 'up'

        elif direction == 'up':
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            direction = 'right'

    return res
print(spiralOrder([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12],
                   [13,14,15,16]]))