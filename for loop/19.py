x=input('Enter a String to check palindorme or not :')
y=''
for i in x:
    y=y+i
    z=y[ : : -1]
if z==x:
    print('Given string is Palindrome')
else:
    print('Given string is not Palindrome')
