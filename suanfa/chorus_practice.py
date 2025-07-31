import bisect
def compute_list(arr):
    res = [0] * len(arr)
    tails = []
    for i in range(len(arr)):
        idx = bisect.bisect_left(tails, arr[i])
        if idx == len(tails):
            tails.append(arr[i])
        else:
            tails[idx] = arr[i]
        res[i] = idx + 1
    return res


while True:
    try:
        lens = int(input())
        alist = list(map(int, input().strip().split()))

        left = compute_list(alist)
        right = compute_list(alist[::-1])
        right = right[::-1]
        anew_list = map(lambda a, b:a+b-1, left, right)
        print(lens - max(anew_list))

    except:
        break