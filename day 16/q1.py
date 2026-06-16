arr = list(map(int, input("Enter array elements: ").split()))

n = len(arr) + 1

total = n * (n + 1) // 2

sum_arr = sum(arr)

missing = total - sum_arr

print("Missing number is:", missing)