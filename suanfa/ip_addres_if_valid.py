"""
bin()是 Python 的内置函数，用于将整数转换为二进制字符串
hex()转16进制
oct()转8进制

int(anumber, 2)表示将这个2进制的啊number转换成十进制
"""
while True:
    try:
        ipadd = input()
        numbers = input()

        ipadd_lis = ipadd.split('.')
        ipadd_lis = [bin(int(i)).replace('0b', '').rjust(8,'0') for i in ipadd_lis]
        tonum = int("".join(ipadd_lis), 2)
        bin_num = bin(int(numbers)).replace("0b","").rjust(32, '0')
        new_ipaddr = f"{int(bin_num[:8],2)}.{int(bin_num[8:16],2)}.{int(bin_num[16:24],2)}.{int(bin_num[24:], 2)}"
        print(tonum)
        print(new_ipaddr)
    except:
        break

