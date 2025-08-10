from collections import Counter

cnt = Counter()
cnt[1] = 5

print(cnt)
print(cnt[0])
print("=======")
for i, v in cnt.items():
    print(i)
    print(v)
