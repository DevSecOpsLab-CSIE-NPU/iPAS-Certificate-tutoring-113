n = open('write.txt','w')
for i in range(5):
    n.write(input() + '\n')
n.close()