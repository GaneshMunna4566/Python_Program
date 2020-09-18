z=[]
for i in range(1,1000):
    y=str(i)[: :-1]
    if str(i)[ : : -1]==str(y)[ : : -1]:
        z.append(i)
print('This are a palindrome numbers from 1 to 1000:')
print(z)
