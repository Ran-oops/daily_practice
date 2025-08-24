from collections import Counter


def equal_frequency(word:str):
    for i in range(len(word)):
        print(word[:i] + word[i+1:])
        cnt = Counter(word[:i] + word[i+1:])
    print(f"cnt:{cnt}")
    print(f"cnt.keys:{cnt.keys()}")
    print(f"cnt.values:{cnt.values()}")

equal_frequency('abcc')