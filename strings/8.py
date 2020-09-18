# wap to count of lowercase in a string

x=input('Enter a string :')
y=0
for i in x:
    if i>='a' and i<='z':
        y=y+1
print('This is you string :',x)
print('This is lower case in string',y)