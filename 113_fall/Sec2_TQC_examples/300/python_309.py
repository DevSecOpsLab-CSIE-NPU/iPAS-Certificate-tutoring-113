total = eval(input())
y = eval(input())
m = eval(input())
print('%s 	  %s' % ('Month', 'Amount'))
for i in range(1, m + 1):
    total += total * y / 1200    
    print('%3d 	 %.2f' % (i, total))