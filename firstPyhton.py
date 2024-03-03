print("Hello, World!")
name="Yasin Beken"
age=34
float=12.2
print(type(name))
print(type(age))
print(type(float))

name="Beken Yasin"
name="B"
name="Beken s"
name="s Yasin"
print(name)
print(name,age,float)
name="Yasin"
age=25
job="Game Developer"
print(f"Name: {name}\nAge: {age}\nJob: {job}")
print("Name: "+name+"\nAge: "+str(age)+"\nJob: "+job)
print("Name:",name,"\nAge:",age,"\nJob:",job)
print("Name: {}\nAge: {}\nJob: {}".format(name,age,job))

# ÇOKLU YORUM SATIRI
print("""Yasin
Beken
Neos""")
print("-----------------")
isim="""Yasin
Beken
Neos"""
print(isim)
print("---------------")
isim="Yasin"
print(isim)
print("Beken")
print("---------------")
print(isim, end=" ")
print("Beken")
print("---------------")
print(*isim,sep="-")
print("---------------")
print("a"*5)
print("---------------")
print(isim[0])
print("---------------")
print(isim[0:3])
print("---------------")
print(isim[0:5:2])
print("---------------")
print(isim[::2])
print("---------------")
print(isim[::-1])
