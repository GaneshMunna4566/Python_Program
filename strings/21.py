# red,white,black,red,green,black

x='red,white,black,red,green,black,black'
y=x.split(',')
z=list()

for i in y:
    if i not in z:
        z.append(i)
        z.sort()
print(z)