from search import search_query
from indexer import indexer

index=indexer()
while True:
    user_query = input("Enter query (or 'exit' to quit): ")
    if user_query.lower() == 'exit':
        break
    results = search_query(user_query, index)
    for doc, score in results[:5]:
        print(doc, score)
