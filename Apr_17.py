'''
#1.check whether a number is prime number or not a prime number
x=int(input("enter the value of x:"))
for i in range(2,x):
    if (x%i==0):
        print(x,"is a not prime number")
        break
else:
    print(x,"is a prime number")

#2.check whether a number is prime number or not in a given interval
x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
u=[]
v=[]
for i in range(x,y+1):
    if i>1:
        for j in range(2,i):
            if(i%j)==0:
                #print(i,"is not a prime number")
                u.append(i)

                break
        else:
            v.append(i)
            #print(i,"is a prime number")
print("List of Non Prime Numbers:", u)
print("Number of Non Prime Numbers:", len(u))
print("List of Prime Numbers:", v)
print("Number of Non Prime Numbers:", len(v))

#3.check whether a number is Armstrong or not
x=int(input("enter the value of x:"))
sum=0
num=x
while x>0:
    di=x%10
    sum=sum+(di*di*di)
    x=x//10
if sum==num:
    print("x is Armstrong number")
else:
    print("x is not Armstrong number")

#4.check whether a number is Armstrong in a given interval

a=int(input("enter the value of x:"))
b=int(input("enter the value of y:"))

c=[]
for num in range(a,b+1):
    a=num
    sum=0
    while num>0: 
        di=num%10
        sum=sum+(di*di*di)
        num=num//10
    if (sum==a):
        c.append(a)
print(c)

#5.find sum of digits of a given number
x=int(input("enter the value:"))

sum=0
while x>0:
    di=x%10
    sum=sum+di
    x=x//10
print(sum)
'''
#6.product of digits
x=int(input("enter the value:"))

pro=1
while x>0:
    di=x%10
    pro=pro*di
    x=x//10
print(pro)
'''
x=[2,-2,3,-3,8,-8,2]
v=[]
u=[]
for i in x:
    if i>=0:
        v.append(i)

    else:
        u.append(i)
#print(v)
#print(u)
#z=sum(v)
#print(z)
z1=sum(u)
c=abs(z1)
#print(c)
if z==c:
        print("equal")
else:
        print("not equal")


x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
for i in range(x,y):
    if i%3==0 and i%5==0:
        print(i, "fizz buzz")
        #continue
    elif i%3==0:
        print(i, "fizz")
        #continue
    elif i%5==0:
        print(i, "buzz")
        #continue
    else:
        print(i, "na")



x=[2,3,4,5,6,7,10,4,10,3,5,6,7,7,8,9,1,2,3,4,5]
u=[]
v=[]
for i in x:
    if i%2==0:
        u.append(i)
    else:
        v.append(i)
print(u)
print(v)
s=sum(u)
print(s)
f=sum(v)
print(f)
if u==v:
    print("equal")
else:
        print("not equal")
        
x=int(input("enter the value:"))
fact=1
for i in range(1,x+1):
    fact=fact*i
print(fact)

 
x=int(input("enter the value:"))
fact=1
i=1
while i>fact:
    fact=fact*i
    i=i+1
print(fact)
'''
