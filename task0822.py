"""
1）Problem:
Given a  of emails, group them by domain name. Normalize each email before grouping:
Remove anything after a + in the username
Ignore dots . in the username
Return a dictionary of {domain: [normalized_email1, ...]}
Input:
["john.doe+ads@gmail.com",
  "john+newsletter@gmail.com",
  "bob@yahoo.com",
  "alice+bob@outlook.com",
  "al.ice@outlook.com"]
Output:
{ 'gmail.com': ['johndoe@gmail.com'],
  'yahoo.com': ['bob@yahoo.com'],
  'outlook.com': ['alice@outlook.com']}
"""

alist = ["john.doe+ads@gmail.com",
  "john+newsletter@gmail.com",
  "bob@yahoo.com",
  "alice+bob@outlook.com",
  "al.ice@outlook.com"]

new_list = []
for i in alist:

    po = i.split("@")[1]
    new_list.append(po)

new_list = list(set(new_list))


adict = dict.fromkeys(new_list, "")
for y in new_list:
    for k in alist:
        if k.endswith(y):
            if not adict[y]:
                adict[y] = [k]
            else:
                adict[y].append(k)

# print(adict)


"""
2）Problem:
You’re given a run-length encoded string of numbers. For example:
"3#5,2#9" → means 3 occurrences of 5, and 2 of 9 → output [5,5,5,9,9]
Input: "3#5,2#9"
Output: [5,5,5,9,9]
"""

def get_output(astr):
    if not astr:
        return []
    else:
        final_li = []
        ali = astr.split(",")
        for u in ali:
            new_ali = u.split("#")
            # num = new_ali[0]
            val = new_ali.pop(0)
            new_ali = new_ali * int(val)
            final_li += new_ali

    print(final_li)


# get_output("3#5,2#9")

"""
3）Problem:
You’re given a list of click-through-rate (CTR) floats. Return the longest contiguous subarray where 
the absolute difference between max and min CTR does not exceed ε (tolerance).
Input: [0.1, 0.15, 0.2, 0.21, 0.19], ε = 0.05
Output: 3  # [0.15, 0.2, 0.21]
"""

def get_result():
    pass

"""
4）Problem:
You are given a list of scheduled ad campaigns, each with a (start_time, end_time) in seconds. 
Return the minimum number of parallel ad slots required to run all campaigns without time overlap.
Input: [(1, 5), (3, 6), (7, 9)]
Output: 2
Explanation:
[1,5] and [3,6] overlap → need 2 slots
[7,9] starts after → reuse
"""
def get_result(alis):
    # for i in alis:
    if not alis:
        return -1
    if len(alis) ==2:
        s1 = set([t for t in range(alis[0][0], alis[0][1])])
        s2 = set([t for t in range(alis[1][0], alis[1][1])])
        if s1 & s2:
            return len(alis)
        else:
            return 1



# print(get_result([(1, 5), (3, 6)]) )

import heapq

def min_parallel_slots(campaigns):
    if not campaigns:
        return 0
    campaigns.sort(key=lambda x: x[0])
    heap = []
    max_slots = 0
    for start, end in campaigns:
        while heap and heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
        if len(heap) > max_slots:
            max_slots = len(heap)
    return max_slots

print(min_parallel_slots([(1, 5), (3, 6), (7, 9)]))































