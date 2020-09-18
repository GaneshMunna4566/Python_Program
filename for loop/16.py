n=int(input('Enter a number for factorial :'))
x=1
if n>=1:
    for i in  range(1,int(n)+1):
        x=x*i
print('Factorial is :',x)