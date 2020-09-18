x=input('Enter a String :')
y= {}
z='a','e','i','o','u'

for i in x:
    if i in z:
        count = x.count(i)
        y[i] = count
print('This are vowels in your string :',y)
