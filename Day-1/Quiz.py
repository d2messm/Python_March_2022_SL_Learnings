name=input("Enter your name:")
score=0
print("Q1. Capital of India:")
print("1. Hyderabad  2. Chennai  3. New Delhi  4. Mumbai")
ans=int(input("Enter your choice:"))
if(ans==3):
    score=score+20

print("Q2. Capital of Bangladesh:")
print("1. Dhaka  2. Chennai  3. New Delhi  4. Mumbai")
ans=int(input("Enter your choice:"))
if(ans==1):
    score=score+20

print("Q3. Capital of Srilanka:")
print("1. Dhaka  2. Chennai  3. New Delhi  4. Colombo")
ans=int(input("Enter your choice:"))
if(ans==4):
    score=score+20

print("Q4. Capital of Australia:")
print("1. Dhaka  2. Canberra  3. New Delhi  4. Colombo")
ans=int(input("Enter your choice:"))
if(ans==2):
    score=score+20

print("Q5. Capital of USA:")
print("1. Washington DC  2. NY  3. New Delhi  4. Colombo")
ans=int(input("Enter your choice:"))
if(ans==1):
    score=score+20

print("Your score is")
print(score)

input()
