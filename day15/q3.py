arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter rotation value: "))

k = k % len(arr)

arr = arr[-k:] + arr[:-k]

print("Right rotated array:", arr)