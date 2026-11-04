from tavily import TavilyClient
import config, os
_client = TavilyClient(api_key=config.TAVILY_API_KEY)
def search(query: str, max_results: int = 5): return _client.search(query, max_results=max_results, include_raw_content=True)["results"]