from utils import clean_text,tokenize
from collections import defaultdict, Counter
import math

def ranker(query, index) :
    
    text=clean_text(query)
    words=tokenize(text)
    query_words=Counter(words)
    scores=defaultdict(float)
    IDF={}
    
    total_docs = len({doc for word in index for doc in index[word]})
    
    for word, w_count in query_words.items() :
        if word not in index:
            continue
        
        num_docs=len(index[word])
        IDF[word]=math.log((total_docs+1)/((num_docs+1)+1))
        
        for doc in index[word] :
            scores[doc]+=index[word][doc]*w_count*IDF[word]
        
    scores=sorted(scores.items(), key=lambda x:x[1], reverse=True)
    return scores
