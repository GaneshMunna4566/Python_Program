x=input('Enter a string :')
y=input('Enter a character to check in main string :')
count=0
for i  in x:
    if y in i:
        count=count+1
print('Total character of',"'"+y+"'",':',count)