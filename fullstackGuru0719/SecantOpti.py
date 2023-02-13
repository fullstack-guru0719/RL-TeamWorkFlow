# Find an approximate value or root(50)

# I think (x ** 3 - 9 =0)
# sol(n): n step approx solution using first derivative

def sol(n):
    if(n > 1):
        result = sol(n-1) - (sol(n-1) ** 3 - 9)/(3 * (sol(n-1) + sol(n-2)))
        return result
    # elif(n==0):
    #     return 1.9
    else:
        return 2
print(sol(3))