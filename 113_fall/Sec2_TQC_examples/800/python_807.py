m=list(map(int,input().split()))
j=sum=0
for i in m:
      sum+=i
      j+=1
print(f'Total = {sum}')
print(f'Average = {sum/j}')