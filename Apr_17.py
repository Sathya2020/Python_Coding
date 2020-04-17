'''x=int(input("enter the value of x:"))
for i in range(2,x):
    if (x%i==0):
        print(x,"is a not prime number")
        break
else:
    print(x,"is a prime number")


x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
for i in range(x,y+1):
    if i>1:
        for j in range(2,i):
            if(i%j)==0:
                break
        else:
            print(i,"is a prime number")



x=[2,3,-4,5,6,-7,10,4,-10,3,-5,6,-7,7,8,-9,1,2,3,4,-5]
v=[]
u=[]
for i in x:
    if i>=0:
        v.append(i)

    else:
        u.append(i)
#print(v)
#print(u)
z=sum(v)
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
        '''
x=str(input("enter the value of x:"))
sum=0
for i in x[0::]:
    sum+=i**3
    if sum==x:
        print(x,"is armstrong number")
    else:
        print(x,"is not armstrong number")
    
'''
while y>0:
    z=y%10
    sum=sum+(z**3)
    if sum==x:
        print("armstrong number")
       
    else:
        print("not armstrong number")
        break
    '''
