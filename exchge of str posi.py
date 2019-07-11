# exchange-str-posi
s=input()
s=list(s)
e=''
for i in range(0,len(s)-1,2):
    tem=s[i+1]
    s[i+1]=s[i]
    s[i]=tem
print(e.join(s))
