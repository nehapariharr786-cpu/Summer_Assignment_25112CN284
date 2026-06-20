r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix:")
for i in range(r):
    matrix.append(list(map(int, input().split())))

for i in range(r):
    sum = 0
    for j in range(c):
        sum += matrix[i][j]

    print("Sum of row", i+1, ":", sum)