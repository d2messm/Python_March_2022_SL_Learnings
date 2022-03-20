n=int(input("Enter any number:"))
counter=0

for i in range(1,n+1):
    if(n%i==0):
        counter=counter+1

if(counter==2):
    print("Prime number")
else:
    print("Not a prime number")
