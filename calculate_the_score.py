from typing import List


def calPoints(operations: List[str]) -> int:
    fin = []
    res = 0
    for i in range(len(operations)):
        if operations[i].isdigit() or operations[i]:
            fin.append(operations[i])
        elif operations[i] == 'C':
            # fin.remove(operations[i-1])
            fin.pop()
        elif operations[i] == 'D':
            # fin.append(operations[i-1] * 2)
            fin.append(int(fin[-1]) * 2)
        elif operations[i] == '+':
            # fin.append(operations[i-1] + operations[i-2])
            fin.append(int(fin[-1]) + int(fin[-2]))
    for j in fin:
        res += int(j)
    return res

print(calPoints(["5","-2","4","C","D","9","+","+"]))




