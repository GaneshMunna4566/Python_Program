# wap tp calculate captial in string

x=input('Enter a string :')
z=0
for i in x:
    if i>='A' and  i<='Z':
        z=z+1
print('This is your string ',x)
print('This are the count of capital letter in your string',z)
