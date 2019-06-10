class Node:
    
    def __init__(self,data,nextNode=None):
        self.data = data
        self.nextNode = nextNode
        
    def setData (self,data):
        self.data = data

    def getData(self):
        return self.data

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self,Node):
        self.nextNode= Node



class LinkedList:

    def __init__(self,head=None):
        self.head=head
        self.size=0

    def addNode(self,data):
        newNode=Node(data,self.head)
        self.head = newNode
        self.size+=1
        return True
    
    def getSize(self):
        return self.size
    
    def printNode(self):
        curr = self.head
        while curr:
            print (curr.data)
            curr= curr.getNextNode()

    def findNode(self,value):
        curr = self.head
        while curr:
            if curr.vaue == value:
                return True
            else:
                curr= curr.getNextNode()
        return False

    def removeNode(self,value):
        prev = None
        curr = self.head

        while curr:
            if curr.getData() == value:
                if prev:
                    prev.setNextNode(curr.getNextNode())
                else:
                    self.head= curr.getNextNode()
                return True
            prev=curr
            curr= curr.getNextNode()

        return False

                    

myList = LinkedList()
print("Inserting")
print(myList.addNode(5))
print(myList.addNode(15))
print(myList.addNode(25))
print("Printing")
myList.printNode()
print("Size")
print(myList.getSize())
print(myList.removeNode(15))
print("Printing")
myList.printNode()
print("Size")
print(myList.getSize())

