"""
valid_words.sort(key=lambda x: x.lower())
"""

while True:
    try:
       alist = input().split()
       alist.pop(0)
       n = int(alist.pop())
       base_words = alist.pop()

       valid_words = [i for i in alist if len(i)==len(base_words) and i != base_words and sorted(list(i))==sorted(base_words)]
       if valid_words:
           valid_words.sort(key=lambda x: x.lower())
           print(len(valid_words))
           print(valid_words[n-1])
       else:
           print(0)

    except:
        break
