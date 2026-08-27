class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def get_pattern(word: str) -> list[int]:
            lookup = {}
            # Maps each unique character to its first-seen index order
            return [lookup.setdefault(char, len(lookup)) for char in word]
        
        target = get_pattern(pattern)
        return [word for word in words if get_pattern(word) == target]