def strStr(haystack: str, needle: str) -> int:
    if needle in haystack:
        return haystack.index(needle)
    return -1


print(strStr('error', 'err'))
