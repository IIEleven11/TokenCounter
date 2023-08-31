## token_counter.py
from tiktoken import Encoding, get_encoding
from typing import Optional

encoding = get_encoding("cl100k_base")


class TokenCounter:
    def __init__(self, query: Optional[str] = ""):
        self.query = query
        self.token_count = 0

    def count_tokens(self) -> int:
        encoding = get_encoding("cl100k_base")
        tokens = encoding.encode(self.query)
        self.token_count = len(tokens)
        return self.token_count
