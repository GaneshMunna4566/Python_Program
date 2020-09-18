x=int(input(('enter a number :')))
y=[]
for i in range(1,x):
    if i%2==0:
        y.append(i)
print(y)
print(sum(y))