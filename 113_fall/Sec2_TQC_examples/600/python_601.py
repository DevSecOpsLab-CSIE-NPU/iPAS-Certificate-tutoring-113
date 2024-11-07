m={}
total=c=0
for i in range(0,12):
   m[i]=int(input())
   if(i%2==0):
     total+=m[i]
for i in range(0,12):
  print('{:>3d}'.format(m[i]),end="")
  c+=1
  if(c==3):
     print()
     c=0
print(total)