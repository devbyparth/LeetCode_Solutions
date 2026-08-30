class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair positions with speeds and sort in descending order of position
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        max_time = 0.0
        
        for pos, spd in cars:
            time = (target - pos) / spd
            # If this car takes strictly more time than the fleet ahead, 
            # it cannot catch up and forms a new fleet
            if time > max_time:
                fleets += 1
                max_time = time
                
        return fleets