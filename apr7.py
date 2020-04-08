'''a="sathiya shanmugam"
print(a.count("s"),a.count("a"))
print(a.replace("h","t"),a.replace(a[9],"a"))

a="python"
print(a.find("h"),a.find("o"),a.find("f"),a.find("g"))

a= "*good morning*"
b = a.strip("*")
print(b)

c = a.strip("(")
print(c)
                     

a= "**value**"
b=a.strip("*")
print(b)

a="_python_"
b=a.lstrip("_")
print(b)

a="_python_"
b=a.rstrip("_")
print(b)

a="good morning"
b=a.split()
print(b)
c=a.split("o")
print(c)
d=a.split("m")
print(d)
'''
a="hello world\n"
b=(a)*100
print(b)
