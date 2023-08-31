from tiktoken import encoding_for_model
from typing import Optional

class TokenCounter:
    def __init__(self, query: Optional[str] = ""):
        self.query = query
        self.token_count = 0

    def count_tokens(self) -> int:
        encoding = encoding_for_model("gpt-4")  # Changed get_encoding to encoding_for_model
        tokens = encoding.encode(self.query)
        self.token_count = len(tokens)
        return self.token_count
