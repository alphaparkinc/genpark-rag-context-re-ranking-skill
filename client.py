class RAGContextReRankingClient:
    def re_rank(self, query: str, documents: list[str]) -> dict:
        return {"re_ranked_documents": sorted(documents, key=lambda d: len(set(d.split()) & set(query.split())), reverse=True)}