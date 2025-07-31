"""
string.isupper()
string.islower()
string.isdigit()
string.count(sub_string)

"""

while True:
    try:
        aa = input()
        a,b,c,d = 0,0,0,0

        for i in aa:
            if i.islower():
                a = 1
            elif i.isupper():
                b = 1
            elif i.isdigit():
                c = 1
            else:
                d = 1

        e = True
        for i in range(len(aa)-2):
            if aa.count(aa[i:i+3]) > 1:
                e = False
                break

        if len(aa)> 8 and (a+b+c+d)>=3 and e:
            print('OK')
        else:
            print('NG')
    except:
        break







