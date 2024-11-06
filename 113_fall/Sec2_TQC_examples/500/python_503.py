def compute(a,b):
    ans=0
    for i in range(a,b+1):
        ans+=i
    return ans
x = eval(input())
y = eval(input())
print(compute(x,y))