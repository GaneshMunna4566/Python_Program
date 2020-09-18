x=int(input(('enter a number :')))
z=int(input(('enter a number :')))
y=[]
for i in range(1,x):
    if i%5==0:
        y.append(i)
print(y)
print(sum(y))