arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))

union = []

for i in arr1 + arr2:
    if i not in union:
        union.append(i)

print("Union of arrays:", union)