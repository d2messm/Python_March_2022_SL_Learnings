data=[14,22,34,36,49,56,59,63,68,75,78,82,83,84,92,92,99]
se=84

low=0
high=len(data)-1
isFound=False

while(True):
    mid=(low+high)//2
    print("High : ",high,"Low : ",low,"Mid : ",mid)

    if(se==data[mid]):
        print("Element found at",mid,"Location")
        isFound=True
        break
    elif(se>data[mid]):
        low=mid
    else:
        high=mid

if(isFound==False):
    print("Element not found")
        
