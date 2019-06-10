p_number= input('Please enter a positive integer\n')
if(int(p_number) < 0):
    print('please enter positive integer only\n')
    exit()
p_number= int(p_number)

def fact(pnumber):
    if(pnumber < 2):
        return 1
    else:
        return pnumber * fact(pnumber-1)

print ('factorial of ' + str(p_number) + ' is ' + str(fact(p_number)))
    
