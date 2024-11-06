for i in range(int(input())):
   data=list(map(float,input().split()))
   print('{:.2f}'.format( max( data ) - min( data )))