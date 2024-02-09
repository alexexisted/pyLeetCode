def findTheDifference(s: str, t: str) -> str:
    res = ''
    for i in range(len(t)):
        if t[i] in s and s.count(t[i]) == t.count(t[i]):
            continue
        else:
            res += t[i]
            return res


# print(findTheDifference('abcd', 'abcde'))
# print(findTheDifference('', 'a'))
print(findTheDifference('abcd', 'abbcd'))
