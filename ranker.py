from utils import clean_text,tokenize
from collections import defaultdict, Counter
import math

def ranker(query, index) :
    
    text=clean_text(query)
    words=tokenize(text)
    query_words=Counter(words)
    scores=defaultdict(lambda : {"match":0,"freq":0})
    results={}
    
    for word, w_count in query_words.items() :
        if word not in index:
            continue
    
        for doc in index[word] :
            scores[doc]["freq"]+=index[word][doc]*w_count
            scores[doc]["match"]+=1
            
    for doc in scores:
        results[doc]=scores[doc]["match"]*1000+scores[doc]["freq"]
        
    results=sorted(results.items(), key=lambda x:x[1], reverse=True)
    return results
