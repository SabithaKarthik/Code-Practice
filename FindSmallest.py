#Given 2 numbers N and K followed by N elements, find the Kth smallest element.If the element cannot be found then print -1
n=list(map(int,input().split()))
inpList=list(map(int,input().split()))
arrSize=n[0]
position=n[1]
i=0
while i<position:
    minimum=min(tuple(inpList))
    inpList=[i for i in inpList if i!=minimum]
    if len(inp)==0 and i<(position-1):
        minimum=-1
        break;
    i=i+1
print(minimum)
