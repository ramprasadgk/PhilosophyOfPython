import requests      
  
def NewsFromBBC(): 
      
    # BBC news api 
    main_url = " https://newsapi.org/v2/everything?q=modi&from=2019-05-18&sortBy=publishedAt&apiKey=d0e27c36e6db402ba8cd7acd29048caf"
  
    # fetching data in json format 
    open_bbc_page = requests.get(main_url).json() 
    
    requests.encoder="utf-8"
    
  
    # getting all articles in a string article 
    article = open_bbc_page["articles"] 
  
    # empty list which will  
    # contain all trending news 
    results = [] 
    source = []
    datep = []
    urls = []
    desc = []
    auth=[]
      
    for ar in article: 
        results.append(ar["title"])
        desc.append(ar["description"])
        auth.append(ar["author"])
        
        srctemp= ar["source"]
        source.append(srctemp["name"])
        datep.append(ar["publishedAt"])
        urls.append(ar["url"])
            
          
    for i in range(len(results)): 
          
        # printing all trending news 
        print(i + 1, source[i],'--->', datep[i] ,'--->', auth[i],'\n--->',results[i] )  
        
                       
  
# Driver Code 
if __name__ == '__main__': 
      
    # function call 
    NewsFromBBC()  