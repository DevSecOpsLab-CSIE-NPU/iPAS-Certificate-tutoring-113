set1 = set()
set2 = set()
set3 = set()
print('Input to set1:')
for i in range(5):
    set1.add(eval(input()))
print('Input to set2:')
for i in range(3):
    set2.add(eval(input()))
print('Input to set3:')
for i in range(9):
    set3.add(eval(input()))
print('set2 is subset of set1:',str(set2.issubset(set1)))
print('set3 is superset of set1:',str(set3.issuperset(set1)))