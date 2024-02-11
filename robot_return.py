"""
    Robot must become at the same position as before
    input can be -->
    R(right)
    L(left)
    U(up)
    D(down)
    """
def judgeCircle(moves: str) -> bool:
    if moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D'):
        return True
    return False


print(judgeCircle('RLRLRRUDDUL'))