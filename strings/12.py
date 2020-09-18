# wap to count the numbers of characters in a string

from collections import Counter
x=input('Enter a string :')
y=dict(Counter(x))
print(y)
