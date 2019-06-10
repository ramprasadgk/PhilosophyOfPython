def div(num):
    try:
        return num/0
    except : ZeroDivisionError
    
print (div(7))