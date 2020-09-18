x=input('Enter a string :')
y=len(x)
if x[-3: ]=='ing':
    print(x+'ly')
elif y>=3:
    print(x+'ing')
elif y<3:
    print(x)
    