n=int(input("Enter any number:"))

isPrime=True

for i in range(2,n):
    if(n%i==0):
        isPrime=False
        break

if(isPrime):
    print("Prime Number")
else:
    print("Not Prime Number")
        
