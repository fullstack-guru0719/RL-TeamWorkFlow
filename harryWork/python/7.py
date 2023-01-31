def checkingprime(num):
    if (num >1):
        for i in range(2, int(num/2)+1):
            if(num  %  i == 0):
                print('It is not prime')
                break
        else:
            print('It is prime')

    else:
        print('It is not prime')
num = int(input('insert number'))

checkingprime(num)
