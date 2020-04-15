'''x=int(input("enter a number: "))
if x==5:
    print("Im Happy")
elif x>5:
    print("Sad")
else:
    print("Nothing")
#print("shut up")

#no. is odd or even
y=int(input("enter the value : "))
#print(y%2==0)
if y%2==0:
    #print("no. is divided by 2")
    print("no. is even")
print("no. is odd")
#no. is odd or even
y=int(input("enter the value : "))
#print(y%2==0)
if y%2==0:
    #print("no. is divided by 2")
    print("no. is even")
else:
    #print("no. is not divided by 2")
    print("no. is odd")


#no. is positive or negative
z=int(input("enter the value of z:"))
print(z>0)
if z>0:
    print("z is positive")
elif z<0:
    print("z is negative")
else :
    print("z is neutral")
print("z is whole number")

#no. is 5 or not
h= int(input("enter the value of h:"))
print(h==5)
if h==5:
    print("h is five")
print("h is not 5")

d=int(input("enter the value of :"))
if d>3:
    print("number is greater than 3")
elif d<8:
    print("no. is less than 8")
else :
    print("no. is not between 3 and 8")

#whether a string is palindrome
s=str(input("enter the string:"))
if s==s[::-1]:
    print("string is palindrome")
else :
    print("string is not palindrome")

m=int(input("enter the mark of student:"))
if 0<=m<=100:
    print("m is valid")
if m==100:
    print("student grade is Grade a")
elif 90<=m<=99:
    print("student grade is Grade b")
elif 80<=m<=89:
    print("student grade is Grade c")
elif 70<=m<=79:
    print("student grade is Grade d")
elif 60<=m<=69:
    print("student grade is Grade e")
elif 0<=m<=49:
    print("student grade is Grade f,fail")
else:
    print("student mark is invalid")
    

s=str(input("enter the string:"))
print(s[0]==s[len(s)//2]==s[-1])
if s[0]==s[len(s)//2]==s[-1]:
    print("all are equal")
else :
    print("not equal")

s=int(input("1.enter two digit number:"))
s1=int(input("2.enter single digit number c:"))
x=s//10
y=s%10
z=x+y
print(z==s1)
if (z==s1):
    print("condition is correct")
else:
    print("condition is wrong")
'''
string=str(input("enter the string:"))
vowels=0
for s in string:
    if (s=='a' or s=='e' or s=='i' or s=='o' or s=='u'):
      vowels = vowels+1
    print(vowels)
    print("number of vowels")
else:
    print("consonant")

      

      
