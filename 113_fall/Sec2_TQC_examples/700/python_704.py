set1 = set()
num = eval(input())
while num!=-9999:
    set1.add(num)
    num = eval(input())
print('Length:',len(set1))
print('Max:',max(set1))
print('Min:',min(set1))
print('Sum:',sum(set1))