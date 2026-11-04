from typing import TypedDict, List
class ResearchState(TypedDict):
    repo_url: str
    sub_questions: List[str]
    search_results: List[dict]
    chunks: List[dict]
    brief: str
    citations: List[dict]
    retries: int
    needs_retry: bool