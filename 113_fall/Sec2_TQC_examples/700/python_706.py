count= eval(input())
alpha=26
for i in range(count):
 sentence = input()
 set1 = set(sentence.lower())
 if ' ' in set1:
     set1.remove(' ')
 if len(set1) >= alpha:
     print('True')
 else:
     print('False')