while True: 
    n=int(input())
    if n==-9999: break
    if(n>0 and n<60):
        print('E')
    elif(n>=60 and n<70):
        print('D')
    elif(n>=70 and n<80):
        print('C')
    elif(n>=80 and n<90):
        print('B')
    elif(n>=90 and n<=100):
        print('A')