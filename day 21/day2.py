string = input("Enter a string: ")

result = ""

for i in string:
    if 'a' <= i <= 'z':
        result += chr(ord(i) - 32)
    else:
        result += i

print("Uppercase string:", result)