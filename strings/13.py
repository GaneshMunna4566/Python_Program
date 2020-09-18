# wap to count the numbers of each word in a string

from collections import Counter

x=input('Enter a String :')
y=x.split()
z=dict(Counter(y))
print('This is repeated word in a string :',z)
