from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    # write code here
    n = len(numbers)
    for i in range(n):
        if numbers[i]> target:
            break
        for j in (i+1, n):
            if numbers[i] +  numbers[j] == target:
                return [i+1, j+1]


print(twoSum([3,2,4],6))