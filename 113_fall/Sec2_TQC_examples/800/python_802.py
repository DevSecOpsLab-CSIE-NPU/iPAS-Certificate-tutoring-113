n=str(input(''))
sum=0
for i in range(0,len(n)):
    sum+=ord(n[i])
    print('ASCII code for ''+n[i]+'' is '+str(ord(n[i])))
print(sum)