#Project based on random module"
print("===================================")
print("Mini Project - Snake Gun Water Game")
print("===================================")
a1=[]
a2=[]
a3=[]
r=int(input("Enter the number of attempts: "))
for i in range(r): #iterate for 10 times
    a=str(input("User Value:")) #getting user input
    import random
    n=["snake","gun","water"]
    x=random.choice(n) #system will select element in the list randomly
    print(x)
    if x==a: 
        x1="tie"
        print(x1)
        a1.append(x1)
    elif (a=="snake" and x=="gun") or (a=="gun" and x=="water") or (a=="water" and x=="snake"):
        x2="System Wins"
        print(x2)
        a2.append(x2)
    else:
        x3="User Wins"
        print(x3)
        a3.append(x3)
print("10 Attempts played")
l1=len(a1)
print("Tie wons %s attempts" %l1)
l2=len(a2)
print("System wons %s attempts" %l2)
l3=len(a3)
print("User wons %s attempts" %l3)
if l2>l3: #comparing number of attempts
    print("So, the Winner is SYSTEM, Congrats")
elif l2==l3:
    print("Both System and User are same number of attempt, Tied")
else:
    print("So, the Winner is USER, Congrats")

print("==================================")
 
