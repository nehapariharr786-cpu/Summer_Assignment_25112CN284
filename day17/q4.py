arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))

common = []

for i in arr1:
    for j in arr2:
        if i == j and i not in common:
            common.append(i)

print("Common elements:", common)