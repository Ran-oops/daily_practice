"""
注意边界值 z 和9
使用chr和ord
"""

while True:
    try:
        ming_pwd = input()
        encrypt_pwd = input()

        encrypted_results = ""
        for i in ming_pwd:
            if i.isdigit():
                i = str(int(i)+1)[-1]
            elif i.isupper():
                i = i.lower()
                i = chr(ord(i)+1) if i != 'z' else 'a'
            elif i.islower():
                i = i.upper()
                i = chr(ord(i)+1) if i != 'Z' else 'A'
            encrypted_results += i

        decrypted_results = ""
        for i in encrypt_pwd:
            if i.isdigit():
                i = str(int(i)-1) if int(i)> 0 else '9'
            elif i.isupper():
                i = i.lower()
                i = chr(ord(i)-1) if i != 'a' else 'z'
            elif i.islower():
                i = i.upper()
                i = chr(ord(i)-1) if i != 'A' else 'Z'
            decrypted_results += i

        print(encrypted_results)
        print(decrypted_results)

    except:
        break