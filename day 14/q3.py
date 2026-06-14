arr = list(map(int, input("Enter array elements: ").split()))

arr = list(set(arr)) 


arr.sort()

if len(arr) >= 2:
    print("Second largest element is:", arr[-2])
else:
    print("Second largest element does not exist")