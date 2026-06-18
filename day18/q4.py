arr = list(map(int, input("Enter sorted array elements: ").split()))

target = int(input("Enter element to search: "))

low = 0
high = len(arr) - 1

found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print("Element found at index:", mid)
        found = True
        break

    elif arr[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

if found == False:
    print("Element not found")