from ranker import ranker

def  search_query(query, index) :
    if not query.strip():
        return []
    results=ranker(query, index)
    return results
