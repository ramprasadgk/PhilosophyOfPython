print('begin')

array = [120, 200, 100, 101, 211, 107]



def partition(array, begin, end):
    
    pivot = begin
    print (pivot)
    for i in range(begin+1, end+1):
        print ('looping', begin+1, end+1)
        if array[i] <= array[begin]:
            pivot += 1
            print(array)
            array[i], array[pivot] = array[pivot], array[i]
            print(array)
    print('final swap')
    array[pivot], array[begin] = array[begin], array[pivot]
    print(array)
    print(pivot)
    return pivot



def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)

quicksort(array)

print(array)