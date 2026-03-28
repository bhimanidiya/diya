
f=open("ONE.TXT","r")
data=f.read()
print("file content:",data)
f.close()

f=open("ONE.TXT","r")
data=f.read(10)
print("first part:",data)
f.close()

f=open("ONE.TXT","r")
line1=f.readline()
line2=f.readline()
line3=f.readline()
print("line1:",line1)
print("line2:",line2)
print("line3:",line3)
f.close()

f=open("ONE.TXT","r")
lines=f.readlines()
print("list of lines:",lines)
print("number of lines:",len(lines))
f.close()


f=open("ONE.TXT","r")
lines=f.readlines()
print(lines[1].strip())
f.close()