from functools import reduce

def mut(num,num2):
    return num * num2


li = [10,20,30,40,50,60,70,80]
print(reduce(mut,li))