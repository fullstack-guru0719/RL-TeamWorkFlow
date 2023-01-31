s1 = float(input('first'))
s2 = float(input('second'))
s3 = float(input('third'))

s = (s1+s2+s3)/2

area = (s*(s-s1)*(s-s2)*(s-s3))**0.5

print('The area is: ', area)
