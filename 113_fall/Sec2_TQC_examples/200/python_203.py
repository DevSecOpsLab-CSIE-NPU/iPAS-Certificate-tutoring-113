n=int(input())
if(n%4==0 and (n%400==0 or n%100!=0)): print(f'{n} is a leap year.')
else : print(f'{n} is not a leap year.')