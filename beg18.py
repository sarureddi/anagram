s1=int(input())
l1=[]
for i in range(0,s1):
    
    l1.append(input())
c1=0
s11=['a','a','b','i','k','l']
for i in l1:
    i=sorted(i)
    if(i==s11):
        c1=c1+1
print(c1)
