x=int(input('Enter a number to check it is palindrome or not :'))
a=str(x)
y=''
for i in a:
    y=str(y+i)
if a== y[:: -1]:
    print('yes',"'{}'".format(x),'it is palindrome')
else:
    print('no')
