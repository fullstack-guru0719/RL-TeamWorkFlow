fib = [0, 1]
n = 9
n = int(input())
while(fib[-1] <= n):
    print(fib[-1])
    fib.append(fib[-1]+fib[-2])
if n in fib:
    print('fib')
else:
    print('wrong')

