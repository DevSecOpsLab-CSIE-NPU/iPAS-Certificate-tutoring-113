f = open("read.txt")
w = f.read()
sp = w.split(" ")
total = 0
for x in sp:
    total += eval(x)
print(total)