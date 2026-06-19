r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix:")
for i in range(r):
    matrix.append(list(map(int, input().split())))

transpose = []

for j in range(c):
    row = []
    for i in range(r):
        row.append(matrix[i][j])
    transpose.append(row)

print("Transpose matrix:")
for i in transpose:
    print(i)