a = int(input())
b = int(input())
total = 0
count = 0
for i in range(a, b + 1):
    if i % 4 == 0 or i % 9 == 0:
        count += 1
        print("{:<4d}".format(i), end="")
        if count % 10 == 0:
            print()
        total += i
print()
print(count)
print(total)