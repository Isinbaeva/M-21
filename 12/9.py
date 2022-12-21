char = input().lower()
text = input().split()
for word in text:
    if char in word.lower():
        print(word)