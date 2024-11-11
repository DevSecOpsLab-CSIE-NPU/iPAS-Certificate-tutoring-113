import math
def compute(x,y):
    gcd = math.gcd(x,y)
    return gcd  
x,y = eval(input())
m,n = eval(input())
q = y*n
p = m*y+x*n
gcd=compute(p,q)
print(f'{x}/{y} + {m}/{n} = {int(p/gcd)}/{int(q/gcd)}')