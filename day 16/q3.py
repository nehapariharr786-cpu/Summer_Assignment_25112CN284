arr = list(map(int, input("Enter array elements: ").split()))

target = int(input("Enter sum value: "))

found = False

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print("Pair found:", arr[i], arr[j])
            found = True

if found == False:
    print("No pair found")