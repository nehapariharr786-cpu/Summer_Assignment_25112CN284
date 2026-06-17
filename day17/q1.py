arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))
arr1.sort()
arr2.sort()
merge = arr1 + arr2
merge.sort()

print("Merged array:", merge)