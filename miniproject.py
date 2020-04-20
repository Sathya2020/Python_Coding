a1=[]
a2=[]
a3=[]
for i in range(10):
    a=str(input("User Value:"))
    import random
    n=["s","g","w"]
    x=random.choice(n)
    print(x)
#print("Random Value: ", random.choice(n))
    if x==a:
        x1="tie"
        print(x1)
        a1.append(x1)
    elif (a=="s" and x=="g") or (a=="g" and x=="w") or (a=="w" and x=="s"):
        x2="Random Wins"
        print(x2)
        a2.append(x2)
    else:
        x3="User Wins"
        print(x3)
        a3.append(x3)
print("10 Attempts played")
#print(a1)
l1=len(a1)
print("Tie wons %s attempts" %(l1))
#print(a2)
l2=len(a2)
print("System wons %s attempts" %l2)
#print(a3)
l3=len(a3)
print("User wons %s attempts" %l3)
if l2>l3:
    print("So, the Winner is SYSTEM, Congrats")
elif l2==l3:
    print("Both System and User are same number of attempt, Tied")
else:
    print("So, the Winner is USER, Congrats")
 
'''
for j in n:
    random.shuffle(j)
    print(j)

#print(a)
'''
