def maxProfit(list):
    length = len(list)
    max = 0
    result = 0
    for i in range(length-1,-1,-1):
        if max > list[i]:
            result +=(max - list[i])
        else:
            max = list[i]

    return result

list = [1,2,3,7,5,6,4]
print(maxProfit(list))
        


        
