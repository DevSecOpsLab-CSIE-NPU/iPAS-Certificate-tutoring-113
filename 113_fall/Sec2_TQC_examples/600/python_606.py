def compute(r,c):
    for i in range(r):
        for j in range(c):
          print("%4d"%(j-i), end='')
        print()
r = int(input())
c = int(input())
compute(r,c)