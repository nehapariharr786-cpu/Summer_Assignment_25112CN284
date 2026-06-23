s = input("Enter string: ")

for ch in s:
    if s.count(ch) > 1:
        print("First repeating character:", ch)
        break
else:
    print("No repeating character")