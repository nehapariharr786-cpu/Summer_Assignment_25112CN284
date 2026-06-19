r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

print("Enter first matrix:")
A = []
for i in range(r):
    A.append(list(map(int, input().split())))

print("Enter second matrix:")
B = []
for i in range(r):
    B.append(list(map(int, input().split())))

result = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(A[i][j] - B[i][j])
    result.append(row)

print("Subtraction of matrices:")
for i in result:
    print(i)