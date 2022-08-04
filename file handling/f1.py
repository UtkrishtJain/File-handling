f=open("test1.txt","r")
print(f.read())  # read the entire file

print(f.read(5),"how are you")
f.close()

g=open("test2.txt","r+")
g.write("hello world")
g.writelines(["ram\n","sham\n","mohan\n"])
l=g.readlines()
print(l)

for x in l:
    print(x)