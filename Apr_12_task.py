a=list()
b=tuple()
c=set()
d=dict()
print(a)
print(b)
print(c)
print(d)
#task1
a=list()
b=[5,6,8,9]
c=a+b
print(c)
d=[8,9,1,5,6,7,8]
e=c+d
print(e.count(8))
#mean
print("mean: ", sum(e)/len(e))
#sum
print("sum: ",sum(e))
#min
print("min: ",min(e))
#max
print("max: ",max(e))
f=set(e)
print(tuple(f))
#median
g=((len(f))+(len(f) + 1))/2
print("median: ",g)

#task 2
A=set()
B=set()
c={7,8,9,1,2,3,4,5,0}
d={4,5,6,0}
A.update(c)
print(A)
B.update(d)
print(B)
e=B.issubset(A)
print(e)
f=B.isdisjoint(A)
print(f)
A.remove(8)
print(A)
B.discard(0)
print(B)
print(sum(A.union(B)))

#task 3
P=(1,4,5,6,7)
Q=(5,6,7,8,9)
c=P+Q
print(c)
d=tuple(set(c))
print(d)
e=d.index(9)
print(e)
h=set(d)
print(h)
f={0,4,5}
print(tuple(h.intersection(f)))
print((tuple(h.intersection(f))*3))
#task4
S={1:[["english","maths","science"],["bio-zoology","bio-botany","physics"]],2:(10,20,40,"python program")}
print(S[1][1][1][4:])
print(len(tuple(S[1][0])))
print(S.keys())
print(S[2][3][:6])
print(S[2][0]+S[2][1]+S[2][2])
#task 5
Z=dict()
Z["hello"]=5
Z["python"]=6
Z["val"]=3
print(Z)
print(Z.keys())
print(Z.values())

