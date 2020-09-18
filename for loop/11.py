x=int(input(('enter a number :')))
z=int(input(('enter a first number to multiply :')))
a=int(input(('enter a second number to multiply :')))
y=[]
for i in range(1,x+1):
    if i%z==0 and i%a==0:
        y.append(i)
print(y)
print(sum(y))