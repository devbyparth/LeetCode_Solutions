from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        ans = [0] * n
        
        # Queue stores original indices: [0, 1, 2, ..., n-1]
        index_q = deque(range(n))
        
        for card in deck:
            # 1. Take the next available spot for the current smallest card
            ans[index_q.popleft()] = card
            
            # 2. Skip the next spot by sending its index to the back of the queue
            if index_q:
                index_q.append(index_q.popleft())
                
        return ans