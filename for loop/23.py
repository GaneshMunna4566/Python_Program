count=0
while count<3:
    username=input('Enter username :')
    password=input('Enter password :')
    if username=='ganesh' and password=='munna4566':
        print('Success full login')
        break
    else:
        print('Username or password is wrong')
        count+=1
print("Attempts are completed")