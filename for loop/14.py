x='46548'
even=0
odd=0
z=[]
for i in x:
    z.append(i)
    if int(i)%2==0:
        even=even+1
    elif int(i)%2!=0:
        odd = odd + 1
print(max(z))
print('even is :',even)
print('odd is :',odd)