astr = "186 186 150 200 160 130 197 200"
alist = list(map(int, astr.strip().split()))
lens = len(alist)
left_smaller, right_smaller = [1] * lens, [1] * lens
for i in range(lens):
    for j in range(i):
        if alist[j] < alist[i]:
            left_smaller[i] = max(left_smaller[j] + 1, left_smaller[i])

for i in range(lens - 1, -1, -1):
    for j in range(lens - 1, i, -1):
        if alist[j] < alist[i]:
            right_smaller[i] = max(right_smaller[j] + 1, right_smaller[i])

new_alist = list(map(lambda a, b: a + b -1, left_smaller, right_smaller))
max_num = max(new_alist)
pick_num = lens - max_num
print(pick_num)







