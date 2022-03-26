try:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    c=a/b
    print(c)
except:
    print("Some error occured. Please contact admin@test.com")
except ValueError:
    print("Only numbers are allowed")
except ZeroDivisionError:
    print("Second number cannot be zero")

finally:
    print("\n\n\n\n\ndesigned by : Meganadh")

input()

