print ('begin')

def bubblesort(U):
    swapped = False
    for i in range(len(U)):
        swapped = False
        for j in range(len(U)-1-i):
            if(U[j] > U[j+1]):
                U[j],U[j+1]= U[j+1],U[j]
                print ("swapped ",U[j], 'and',U[j+1])
                swapped = True
                print (U)
            else:
                print ("No need to swap ",U[j], 'and',U[j+1])
                print(U)
        if not swapped:
            return
    

if __name__ == '__main__':
    unsorted = [3,-3,-1]
    bubblesort(unsorted)

print('done')
    