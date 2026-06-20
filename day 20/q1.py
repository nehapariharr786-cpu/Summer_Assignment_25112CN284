r1 = int(input("Enter rows of first matrix: "))
c1 = int(input("Enter columns of first matrix: "))

print("Enter first matrix:")
A = []
for i in range(r1):
    A.append(list(map(int, input().split())))

r2 = int(input("Enter rows of second matrix: "))
c2 = int(input("Enter columns of second matrix: "))

print("Enter second matrix:")
B = []
for i in range(r2):
    B.append(list(map(int, input().split())))

result = []

for i in range(r1):
    row = []
    for j in range(c2):
        sum = 0
        for k in range(c1):
            sum += A[i][k] * B[k][j]
        row.append(sum)
    result.append(row)

print("Multiplication of matrices:")
for i in result:
    print(i)