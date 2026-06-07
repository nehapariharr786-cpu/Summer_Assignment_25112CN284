def reverse_num(n):
    if n < 10:
        print(n, end="")
    else:
        print(n % 10, end="")
        reverse_num(n // 10)

num = int(input("Enter a number: "))

print("Reversed number =", end=" ")
reverse_num(num)