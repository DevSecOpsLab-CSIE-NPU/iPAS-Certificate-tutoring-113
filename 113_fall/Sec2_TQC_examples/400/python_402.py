n= []
while True:
    value = eval(input())
    if value == 9999:
        break
    n.append(value)
print(min(n))