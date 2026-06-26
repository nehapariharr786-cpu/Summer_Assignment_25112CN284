sentence = input("Enter words: ")

words = sentence.split()

words.sort(key=len)

print("Words sorted by length:")
for word in words:
    print(word)