x='technosoft'
y=len(x)
if y>2:
    print(f"'{x[0:2]+x[-2:]}'")
elif y==2:
    print(f"'{x*2}'")
else:
    print('Empty string')