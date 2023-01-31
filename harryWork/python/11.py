num = int(input('Insert'))

lenth = len(str(num))

number = num
sum = 0
while(number !=0):
    rem =  number %10
    sum += (rem**lenth)
    number  = number //10
    print(number)
if(sum == num):
    print('THis is arms')
else:
    print('No')