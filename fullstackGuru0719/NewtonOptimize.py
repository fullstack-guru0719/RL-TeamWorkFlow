# Find an approximate value or root(50)

# I think (x*x - 50 =0)
# sol(n): n step approx solution
def sol(n):
    if(n > 0):
        result = sol(n-1) - (sol(n-1)**2 - 50 )/(2 * sol(n-1))
        return result
    else:
        return 7

print(sol(3))

