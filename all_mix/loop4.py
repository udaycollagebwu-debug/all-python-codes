name = input ("Enter your name :")
age = int (input ("Enter your age :"))
hoby = input ("Enter your hoby (like geming,droing,danceing)")
for i in name:
    c=name[i]
    if c == 'a':
        print(name.upper())
    else:
        print(name.lower())
    
        