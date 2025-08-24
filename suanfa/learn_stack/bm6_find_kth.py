from typing import List
import bisect

def findKth(a: List[int], n: int, K: int) -> int:
    # write code here
    for i in range(K):
        swapped = False
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break

    return a[-K]

print(findKth([1,3,5,2,2],5,3))