def mergeAlternately(word1: str, word2: str) -> str:
    res = ''
    ind = 0
    while len(word1) > ind and len(word2) > ind:
        res += word1[ind]
        res += word2[ind]
        ind += 1

    while len(word1) > ind:
        res += word1[ind]
        ind += 1

    while len(word2) > ind:
        res += word2[ind]
        ind += 1

    return res

print(mergeAlternately('hello', 'world'))

