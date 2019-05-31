l=[]
t=int(input())
a=""
b=""
s=""
if 1<=t<=10:
    for i in range(t):
        l.append(input())


for i in range(0,len(l[0]),2):
    a=a+s[i]
    b=b+s[i+1]

print(a+b)
