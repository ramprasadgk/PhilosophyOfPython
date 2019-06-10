class MaxHeap:
    def __init__(self,items=[]):
       # super.__init__()
        self.heap=[0]
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap)-1)

    def push(self,data):
        self.heap.append(data)
        self.__floatUp(len(self.heap)-1)
        
    def peek(self):
        if(self.heap[1]):
            return self.heap[1]
        else:
            return False
    def pop(self):
        if (len(self.heap) > 2):
            self.__swap(1,len(self.heap)-1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) ==2:
            max=self.heap.pop()
        else:
            max=False
        return max
    def __swap(self,i,j):
        self.heap[i],self.heap[j] =  self.heap[j],self.heap[i]
    def __floatUp(self,i):
        parent = i//2    
        if i <=1:
            return 
        elif self.heap[i] > self.heap[parent]:
            self.__swap(i,parent)
            self.__floatUp(parent)

    def __bubbleDown(self,i):
        left = i * 2
        right = i * 2 + 1
        max = i
        
        if len(self.heap) > left and self.heap[left] > self.heap[max]:
            max = left
        if len(self.heap) > right and self.heap[right] > self.heap[max]:
            max = right
        if(max != i):
            self.__swap(i,max)
            self.__bubbleDown(max)
            
            
m = MaxHeap([95,3,21])
m.push(10)  
print (str(m.heap[0:len(m.heap)]))
print(str(m.pop()))
m.push(34)
print (str(m.heap[0:len(m.heap)]))
print(str(m.pop()))
print(str(m.pop()))
print(str(m.pop()))
print(str(m.pop()))
print(str(m.pop()))
        
        
            
    
        
        