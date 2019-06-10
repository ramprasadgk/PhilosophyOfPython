import os

dirstructure={}
files={}
dirs={}

 
rootDir = 'C:\\Users\\Public\\test'
for dirName, subdirList, fileList in os.walk(rootDir):
    dirstructure[dirName]={}
    print('==>',dirName, subdirList, fileList,'<==')

    #print('Files inside directory: %s' % dirName)
    for fname in fileList:
        #print('\t%s' % fname)
        files[os.path.abspath(fname)]=[]      
        
    dirstructure[dirName]['files']= files
    files={}
    

    #print('directoris inside directory: %s' % dirName)
    for dname  in subdirList:
        #print('\t%s' % dname)
        dirs[os.path.abspath(dname)]=[]
    
    dirstructure[dirName]['dirs']= dirs
    dirs={}


for key, value in dirstructure.items():
    print(key)
    for k,v in value.items():
        print (k,v)
      