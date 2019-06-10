def is_palindrome(str):
    #print(str)
    start = 0
    end = len(str)-1
    while(start < end):
        if(str[start] !=  str[end]):
            return False
        start += 1
        end -= 1
    
    return True


str = "fuckyouuoyk";
longest = 0
longp = ""
lens = len(str)
for i in range(1,lens):
    for j in range(i,lens):
        pal = str[j:]
        if (is_palindrome(pal)):
            l = len(pal)
            if(longest < l):
                longest =l
                longp= pal
                
print (longest,longp)
                
    
    


            
    