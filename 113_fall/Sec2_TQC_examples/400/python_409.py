count1 = 0
count2 = 0
null = 0
for i in range(5):
    vote = int(input())
    if  vote == 1:
        count1 += 1
    elif  vote == 2:
        count2 += 1
    else:
        null += 1    
    print("Total votes of No.1: Nami =  %d" % count1)
    print("Total votes of No.2: Chopper =  %d" % count2)
    print("Total null votes =  %d" % (null))
if count1 > count2:
    print("=> No.1 Nami won the election.")
elif count1 < count2:
    print("=> No.2 Chopper won the election.")
else:
    print("=> No one won the election.")