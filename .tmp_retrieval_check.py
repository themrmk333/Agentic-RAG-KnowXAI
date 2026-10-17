from rag.retrieval.semantic_retriever import SemanticRetriever

query = "My laptop is connected to Wi-Fi, but I cannot access the internet. What should I do?"

try:
    retriever = SemanticRetriever()
    results = retriever.retrieve_with_metadata(query=query, top_k=5)

    print("RESULT COUNT =", len(results))

    for i, result in enumerate(results, 1):
        print(f"\n--- RESULT {i} ---")
        print("Similarity:", result["similarity_score"])
        print("Document:", result["document_title"])
        print("Source:", result["source_path"])
        print("Content:")
        print(result["content"][:1000])

except Exception as e:
    print("ERROR:", repr(e))
