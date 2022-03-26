def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def nCr(n,r):
    return factorial(n)/(factorial(n-r)*factorial(r))
def nPr(n,r):
    return factorial(n)/factorial(n-r)
