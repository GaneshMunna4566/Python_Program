# wap to accept a hyphen seperated of words and sort as alphabetically

x=input("Enter a hyphen separated sequence of words:")
y=x.split('-')
for i in y:
    y.sort()
print('This is your string :'+ ' '+x)
print('After sorted this is a alphabetically order in given string :'+ ' ' +'-'.join(y))