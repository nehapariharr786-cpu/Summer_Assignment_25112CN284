n = int(input("Enter size of matrix: "))

matrix = []

print("Enter matrix:")
for i in range(n):
    matrix.append(list(map(int, input().split())))

symmetric = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            symmetric = False
            break

if symmetric:
    print("Matrix is Symmetric")
else:
    print("Matrix is Not Symmetric")