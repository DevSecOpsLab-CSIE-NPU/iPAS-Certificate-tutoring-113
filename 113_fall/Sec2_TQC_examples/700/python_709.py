d= {}
while True:
    key = input('Key: ')
    if key == 'end': 
        break
    d[key] = input('Value: ')
for i in sorted(d.keys()):
    print(i+': '+d[i])