a = 5 # a = float(input('Enter first side: '))

b = 6 # b = float(input('Enter second side: '))

c = 7 # c = float(input('Enter third side: '))

s = (a + b + c) / 2 # calculate the semi-perimeter

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print('The area of the triangle is %0.2f' %area)