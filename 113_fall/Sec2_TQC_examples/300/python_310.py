x=eval(input())
i=1
tmp=0
while i<x:
    tmp+=1/((i**0.5)+((i+1)**0.5))
    i+=1
print('%.4f'%(tmp))