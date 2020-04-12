a=[3,4,5,5,6,7,8]
a.clear()
print(a)
a=[3,4,5,5,6,7,8]
del(a)
print(a)
#copy
a=[3,4,5,5,6,7,8]
b=a.copy()
a.append(9)
print(a)
print(b)
#direct assignment
a=[3,4,5,5,6,7,8]
b=a
a.append(1)
print(a)
print(b)
#list to tuple
a=[1,2,3,4,5,6,7,8,9]
b=tuple(a)
print(b)
#list to set
a=[1,2,3,4,5,6,7,8,9]
b=set(a)
print(b)
#tuple to list
a=(1,2,3,4,5,6,7,8,9)
b=list(a)
print(b)
#tuple to set
a=(1,2,3,4,5,6,7,8,9)
b=set(a)
print(b)
#set to list
a={1,2,3,4,5,6,7,8,9}
b=list(a)
print(b)
#set to tuple
a={1,2,3,4,5,6,7,8,9}
b=tuple(a)
print(b)
a=(1,2,3,4,5,5,6,7,8,9)
b=a.count(5)
print(b)
a=(1,2,3,4,5,5,6,7,8,9)
print(a[4])
a=(1,2,3,4,5,5,6,7,8,9)
del(a)
print(a)

#remove duplicates
a=(1,2,2,3,4,5,5,6,7,8,8,9,9)
b=set(a)
print(b)


                                                          
