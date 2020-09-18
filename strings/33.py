x='ganesh munna hello kiran'
z=[]
for i in x.split():
    y=i[0].upper()+i[1:-1]+i[-1].upper()
    z.append(y)
print(z)