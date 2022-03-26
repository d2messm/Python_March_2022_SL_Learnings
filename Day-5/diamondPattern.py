n=int(input("Enter row:")) #5
#for number of rows
for r in range(1,n):
    #Top Half
    for s in range(n,r,-1):
        print(" ",end="")
    for st in range(1,2*r):
        print("*",end="")
    print("")
#Second Half
for r in range(n,0,-1):
    for s in range(n,r,-1):
        print(" ",end="")
    for st in range(1,2*r):
        print("*",end="")
    print("")
