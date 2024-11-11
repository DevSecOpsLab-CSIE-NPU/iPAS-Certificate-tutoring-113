def compute(a,b,c):
    q=b**2-4*a*c
    if q<0:
        print("Your equation has no root.")
    elif q==0:
        print(-b/2*a)
    else:
        q1=(-b+q**0.5)/(2*a)
        q2=(-b-q**0.5)/(2*a)
        print('{}, {}'.format(q1, q2))
a=int(input())
b=int(input())
c=int(input())
compute(a,b,c)