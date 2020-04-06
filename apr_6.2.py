a="python"
b=a[0:1]+a[1].upper()+a[2:4]+a[4].upper()+a[5:]
print(b)
b=a[0].upper()+a[1:3]+a[3].upper()+a[4:5]+a[5].upper()
print(b)

a="python"
b="java"
c=a[0].upper()+a[1:-1]+a[-1].upper()
d=b[0].upper()+b[1:-1]+b[-1].upper()
print(c+d)

q="python"
w=7
e=str(w)
print(type(e))
print((q*w)+(e*len(q)))


r="Fire"
t=5
y=str(t)
print((r*t)+(y*len(r)))
