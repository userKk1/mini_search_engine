import os
from utils import clean_text, tokenize
from collections import defaultdict

def indexer():
    docs=os.listdir("data/documents")
    index=defaultdict(lambda : defaultdict(int))
    
    for doc in docs:
        path=os.path.join("data/documents",doc)
        
        with open(path,"r") as f:
            text=f.read()
            text=clean_text(text)
            words=tokenize(text)
            
            for word in words :
                index[word][doc]+=1
                
    return index
