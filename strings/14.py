# wap to check if a substring is in main string or not

x='python is simple and it is easy'
string=x.split()
substring=input('Enter a word to check :')
if substring in string:
    print('substring\t'+ f'"{substring}"' +'\tis "in" main string')
else:
    print('substring\t'+ f'"{substring}"' +'\tis "not" in main string')
