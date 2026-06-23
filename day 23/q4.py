s = input("Enter string: ")

max_count = 0
max_char = ''

for ch in s:
    if s.count(ch) > max_count:
        max_count = s.count(ch)
        max_char = ch

print("Maximum occurring character:", max_char)
print("Frequency:", max_count)