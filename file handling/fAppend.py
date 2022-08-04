# appending file
f=open("test1.txt","a")
f.writelines(["suman","ram"])
f.close()

g=open("test1.txt","r")
print(g.read(5))

g.seek(0)   # bring file cursor to initial position

print(g.read(10))