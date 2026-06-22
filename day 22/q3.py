string = input("Enter a string: ")

for i in string:
    if i != " ":
        count = 0

        for j in string:
            if i == j:
                count += 1

        print(i, ":", count)