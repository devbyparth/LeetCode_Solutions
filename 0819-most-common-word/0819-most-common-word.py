import re
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)

        words = re.findall(r'\w+', paragraph.lower())

        count = Counter(word for word in words if word not in banned_set)

        return count.most_common(1)[0][0]