# wap to delete nth index from string
x= input('Enter a string :')
y=int(input('Enter index to delete :'))
z=x[:y]+x[y+1:]
print('deleted element from '+ x + "  "+'is :', x[y])
print(z)