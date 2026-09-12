words = ["cat", "elephant", "dog", "hippopotamus"]

# Rule: keep only words longer than 3 letters
long_words = []
for w in words:
    if(len(w) >3):
        long_words.append(w)

print(words)
print(long_words)        