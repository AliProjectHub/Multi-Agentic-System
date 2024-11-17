# agent_state.py
from typing import List, Optional
from typing_extensions import TypedDict

class AgentState(TypedDict, total=False):
    query: str
    question: str
    category: str
    grades: List[str]
    llm_output: Optional[str]
    documents: List[str]
    on_topic: bool
