from typing import List

def plusOne(digits: List[int]):
    string = ''

    for i in digits:
        string += str(i)

    digits.clear()
    fin_int = int(string) + 1

    for j in str(fin_int):
        digits.append(int(j))

    return digits

print(plusOne([9, 9, 9]))