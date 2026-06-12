def perfect(n):
    sum_div = 0

    for i in range(1, n):
        if n % i == 0:
            sum_div += i

    return sum_div == n

num = int(input("Enter a number: "))

if perfect(num):
    print("Perfect Number")
else:
    print("Not a Perfect Number")