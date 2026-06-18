arr = list(map(int, input("Enter array elements: ").split()))

n = len(arr)

for i in range(n):
    for j in range(i+1, n):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print("Descending order:", arr)