# wap to calculate no of words and the no of character in a string

x = input('Enter a string :')
y = x.split()
z=0
for i in x:
    z=z+1
print('no of words in given string :',len(y))
print('no of characters in a string :',z)
