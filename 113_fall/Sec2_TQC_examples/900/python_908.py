fn, num = input(), eval(input())
f = open(fn, 'r')
w = f.read()
sp1 = w.split()
setsp1 = sorted(set(sp1))
for i in setsp1:
    if sp1.count(i) == num:
        print(i, end='\n')