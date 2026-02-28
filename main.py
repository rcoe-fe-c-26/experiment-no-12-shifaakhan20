# AIM: Develop a Python program that reads a text file and 
# prints words of specified lengths (e.g., three, four, 
# five, etc.) found within the file.
# Coder: Shifaa
# Date: 01/03/2026

print("--- Extracting Words from Text File ---\n")

with open("data.txt", "r") as f:
    text = f.read()

length = int(input("Enter length of words: "))

words_set = set()

for word in text.split():
    if len(word) == length:
        words_set.add(word.lower())

sorted_words = sorted(words_set)

print(f"Words with length {length} are:")
print(sorted_words)


