text = input("Enter a line: ")

count = 0
for char in text:
    
    if char.isalpha():
        count = count + 1

print("Total alphabets:", count)