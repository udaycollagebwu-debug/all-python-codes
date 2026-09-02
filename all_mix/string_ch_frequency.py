string = input("Enter a string :")

frequency = {}   # this is a empty Dictionary 

for ch in string:
    if ch in frequency:
        if ch == " ":
            pass
        else:
            frequency[ch]+=1
    else:
        if ch == " ":
            pass
        else:
            frequency[ch]=1


print("The charcter frequency is :")
for ch,count in frequency.items():
    print(ch," : ",count)