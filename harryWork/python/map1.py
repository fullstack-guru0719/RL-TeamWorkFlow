carts = [['smartphone', 400],
        ['Tablet', 450],
        ['laptop', 700]
    ]

Tax = 0.1
# carts = map(lambda item:[item[0], item[1], item[1]*Tax], carts)
# print(list(carts))
def bonus(bonu):
    return [bonu[0], bonu[1], bonu[1]*Tax]
carts = map(bonus, carts)
print(list(carts))