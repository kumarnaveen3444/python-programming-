a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

result = [x + y + z for x, y, z in zip(a, b, c)]# zip is like to use to add (a b c) in terms of (1 + 4 + 7 = 12)

print(result)