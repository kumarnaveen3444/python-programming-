months = [
    "January", "February", "March", "April", 
    "May", "June", "July", "August", 
    "September", "October", "November", "December"
]

num = int(input("Enter month number (1-12): "))

if 1 <= num <= 12:

    print("Month:", months[num - 1])

else:

    print("Please enter between 1 and 12")