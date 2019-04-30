#from math import factorial
print("begin")
input_array= [5]
print ("factorial of 4 is 4*3*2*1 which is 24")

factorial_out=1

def factorial(i):
    if(i == 0):
        return 1
    if (i== 1):
        return 1
    return i * factorial(i-1)
    
print(factorial(input_array[0]))
