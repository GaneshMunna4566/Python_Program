x=input('Enter a string :')
y=input('Enter vowel :')
z=''
for i in x:
    if i not in y:
       z=z+i
print(z)