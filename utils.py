stop_words={"a","an","the","in","at","on","or","and","with","is","are","they",
            "but","you","it","we","before","after","he","she","to","from","was",
            "were","had","have","each","every","be","being","through","within","of","into","between","if"}

def clean_text(text) :
    text=text.lower()
    clean=""
    
    for char in text :
        if char.isalpha() or char==" " :
            clean += char
            
    return clean
    
    
def tokenize(text) :
    words=text.split()
    tokens = []
    
    for word in words :
        if word not in stop_words :
            tokens.append(word)
            
    return tokens
