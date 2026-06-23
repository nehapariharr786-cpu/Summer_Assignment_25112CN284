s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

if sorted(s1) == sorted(s2):
    print("Strings are anagram")
else:
    print("Strings are not anagram")