r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix:")
for i in range(r):
    matrix.append(list(map(int, input().split())))

for j in range(c):
    sum = 0
    for i in range(r):
        sum += matrix[i][j]

    print("Sum of column", j+1, ":", sum)