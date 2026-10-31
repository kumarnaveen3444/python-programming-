letter = 'E'

letter = letter.lower()

if letter in 'aeiou':

    print(f"'{letter}' is a vowel.")

elif letter.isalpha():

    print(f"'{letter}' is a consonant.")

else:
    
    print("That is not a valid alphabet letter.")