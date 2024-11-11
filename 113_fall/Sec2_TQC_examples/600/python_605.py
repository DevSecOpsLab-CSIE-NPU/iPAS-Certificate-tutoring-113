n=[]
for i in range(10):
  x=eval(input())
  n.append(x)
s=sum(n)-max(n)-min(n)
print(s)
print("%.2f"%(s/(10-2)))