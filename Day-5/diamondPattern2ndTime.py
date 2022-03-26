n=int(input("Enter number:"))

#top half
for r in range(1,n):
    #spaces
    for s in range(n,r,-1):
        print(" ",end="")
    #for stars
    for st in range(1,2*r):
        print("*",end="")
    print("")

#bottom half
for r in range(n,0,-1):
    #spaces
    for s in range(n,r,-1):
        print(" ",end="")
    #for stars
    for st in range(1,2*r):
        print("*",end="")
    print("")
