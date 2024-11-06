for i in range(int(input())):
    n=str(input())
    a = [int(j) for j in list(str(n))]
    print("Sum of all digits of "+str(n)+" is "+str(sum(a)))