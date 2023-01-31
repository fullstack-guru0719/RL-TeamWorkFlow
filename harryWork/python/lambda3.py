def times(n):
    return lambda x:x*x
double = times(2)

result = double(2)
print(result)
result = double(3)
print(result)