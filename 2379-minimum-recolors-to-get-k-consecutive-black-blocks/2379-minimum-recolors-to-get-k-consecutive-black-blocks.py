class Solution(object):
    def minimumRecolors(self, blocks, k):
        current_whites = blocks[:k].count('W')
        min_recolor = current_whites

        for i in range(k, len(blocks)):
            if blocks[i-k] == 'W':
                current_whites -= 1
            
            if blocks[i] == 'W':
                current_whites += 1
            
            min_recolor = min(min_recolor, current_whites)
        
        return min_recolor