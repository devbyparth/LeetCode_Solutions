class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        
        # 1. Calculate base satisfied customers
        base_satisfied = sum(c for c, g in zip(customers, grumpy) if g == 0)
        
        # 2. Compute extra satisfied for the first window
        current_extra = sum(customers[i] for i in range(minutes) if grumpy[i] == 1)
        max_extra = current_extra
        
        # 3. Slide the window across the rest of the array
        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                current_extra += customers[i]
            if grumpy[i - minutes] == 1:
                current_extra -= customers[i - minutes]
                
            max_extra = max(max_extra, current_extra)
            
        return base_satisfied + max_extra