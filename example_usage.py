from client import RAGContextReRankingClient
client = RAGContextReRankingClient()
print(client.re_rank("apple fruit", ["apple pie is tasty", "banana is yellow", "an apple a day"]))