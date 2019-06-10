a=[4,6,8]
b = [3,5,7,9]
s=[]
i=0
j=0


while i < len(a) and j < len(b):
   if a[i] < b[j]:
       s.append(a[i])
       i+=1
       
   else: 
       s.append(b[j])
       j+=1
       
       
while i < len(a):
    s.append(a[i])
    i+=1
    
           
while j < len(b):
    s.append(b[i])
    j+=1
    
print (s)
    
    
     
        