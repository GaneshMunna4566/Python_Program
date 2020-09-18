# 'hello','good','morning','to','one','and','all'

x=input('enter a string :')
z=x.split(',')
y=list(z)
a=''
for i in y:
    if len(i)>len(a):
       a=i
       z=a.split()
       for j in z:
         if len(j)>=5:
          print(a)