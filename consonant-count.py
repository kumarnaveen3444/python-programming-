word = "PYTHON"

consonant_count = 0

for letter in word:

    if letter.lower() not in "aeiou":
        
        consonant_count = consonant_count + 1

print("Total consonants:", consonant_count)