word = "python"
stack = []

for letter in word:
    stack.append(letter)

reversed_word = " "
while stack:
    reversed_word += stack.pop()
    
print(reversed_word)