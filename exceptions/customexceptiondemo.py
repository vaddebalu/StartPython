from CustomException import NumberLimitException
def displayNums(num):
    if(num>10):
        raise NumberLimitException
    else:
        for i in range(num):
            print(i)
try:
    displayNums(10)
except Exception as e:
    print("Number limit exceeded")
