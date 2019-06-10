print('begin')

unsorted = [2,5,3,4]

def getpivot(array,begin,end):
    pivot = begin
    for i in range(begin+1,end+1):
        if(array[i] <= array[begin]):
            pivot +=1
            array[i],array[pivot]= array[pivot],array[i]
    array[pivot],array[begin]= array[begin],array[pivot]
    return (pivot) 
            
    




def qsort(array,begin=0,end='None'):
    if end == 'None':
        end = len(array)-1;
    def _quicksort(array,begin,end):
        if(begin >= end):
            return 
        pivot= getpivot(array,begin,end)
        _quicksort(array,begin,pivot-1)
        _quicksort(array,pivot+1,end)
    return _quicksort(array,begin,end)
        
        
        
qsort(unsorted,0,len(unsorted)-1)
print (unsorted)
    
