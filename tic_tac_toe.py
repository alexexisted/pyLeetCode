from typing import List
def tic(moves: List[List[int]]) -> str:
    if len(moves) < 5:
        return "Pending"
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(moves)):
        if i % 2:
            grid[moves[i][0]][moves[i][1]] = "B"
        else:
            grid[moves[i][0]][moves[i][1]] = "A"
    for i in range(len(grid)):
        if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] != 0:
            return grid[i][0]
        elif grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] != 0:
            return grid[0][i]
        elif i == 0 and grid[i][i] == grid[i + 1][i + 1] == grid[i + 2][i + 2] and grid[i][i] != 0:
            return grid[i][i]
        elif i == 2 and grid[i][0] == grid[i - 1][i - 1] == grid[0][i] and grid[i][0] != 0:
            return grid[i][0]
    return "Draw" if len(moves) == 9 else "Pending"


print(tic([[0,0],[2,0],[1,1],[2,1],[2,2]]))

