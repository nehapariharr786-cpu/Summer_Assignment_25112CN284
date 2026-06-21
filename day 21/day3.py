string = input("Enter a string: ")

vowels = 0
consonants = 0

for i in string:
    if i.lower() in "aeiou":
        vowels += 1
    elif i.isalpha():
        consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)