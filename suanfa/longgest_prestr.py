def longestCommonPrefix(strs):

    res = ""
    if not strs:
        print(res)
        return res
    min_str = min(strs, key=lambda x:len(x))
    print(f"min_str:{min_str}")

    for i in range(len(min_str)):
        print(i)
        tmp = min_str[:i+1]
        if not all(item.startswith(tmp) for item in strs):
            break
        else:
            res = tmp


    return res

# print(longestCommonPrefix(strs = ["abca","abc","abca","abc","abcc"]))
# print(longestCommonPrefix(strs = ["abc"]))
print(longestCommonPrefix(strs = ["a"]))