n=int(input())
inpList=list(map(int,input().split()))
outList=[]
for i in range(n):
    j=i+1
    s=sum(inpList[:j])
    if s%2==0:
        outList.append(s)
    else:
        outList.append(l[i])
for i in range(len(outList)):
    if i==(len(outList)-1):
        print(outList[i])
    else:
        print(outList[i],end=" ")
