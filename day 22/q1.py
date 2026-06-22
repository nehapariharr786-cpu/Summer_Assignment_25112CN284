string = input("Enter a string: ")

reverse = ""

for i in string:
    reverse = i + reverse

if string == reverse:
    print("String is Palindrome")
else:
    print("String is Not Palindrome")