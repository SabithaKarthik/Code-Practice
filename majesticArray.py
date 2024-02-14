n=int(input())
inpList=list(map(int,input().split()))
firstSum=sum(inpList[0:3])
lastSum=sum(inpList[-3:])
if firstSum==lastSum:
    print(1)
else:
    print(0)
