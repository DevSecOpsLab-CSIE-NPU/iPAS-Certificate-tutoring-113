t=0
for i in range(5):
   n=str(input())
   if(n=='J'):   t+=11
   elif(n=='Q'): t+=12
   elif(n=='K'): t+=13
   elif(n=='A'): t+=1
   else :   t+=int(n)
print(t)