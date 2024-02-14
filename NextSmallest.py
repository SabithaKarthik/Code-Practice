arrSize=int(input())
n=list(map(int,input().split()))
s=0
out=[]
for i in range(arrSize):
    j=i+1
    while j<arrSize:
        if n[i]>n[j]:
            s=n[j]
            break
        j=j+1
    if s!=0:    
        out.append(s)
        s=0
    else:
        out.append(-1)
for i in range(len(out)):
    if i==(len(out)-1):
        print(out[i])
    else:
        print(out[i],end=" ")
    
