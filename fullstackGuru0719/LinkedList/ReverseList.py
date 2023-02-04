
def reverseString(str,num):
    if len(str) <= num:
        return str[::-1]
    else:
        return reverseString(str[:num],num)+reverseString(str[num:],num)

print(reverseString("12343456",4))


