"""
letters.sort(key=lambda x:x.lower())
letters.reverse()
"""

while True:
    try:
        astring = input()
        # astring = "BabA"
        letters = [i for i in astring if i.isalpha()]
        print(letters)
        letters.sort(key=lambda x:x.lower())
        letters.reverse()
        print(letters)
        result = ""
        for i in astring:
            if i.isalpha():
                result += letters.pop()
            else:
                result += i

        print(result)
    except:
        break