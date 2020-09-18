x=int(input('Enter a number to check given number is armstrong :'))
a=str(x)
count=0
y=''
for i in a:
    count =count+int(i)**3
    y=count
print(y)
if str(a)==str(y):
    print('Given number is armstrong number')
else:
    print('Given number is not armstrong number')