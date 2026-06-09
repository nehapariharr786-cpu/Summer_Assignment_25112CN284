n = 5

for i in range(n):
    ch = chr(65 + i)
    for j in range(i + 1):
        print(ch, end="")
    print()