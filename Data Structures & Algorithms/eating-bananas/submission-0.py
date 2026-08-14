class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        eating_rate = high

        while low <= high:
            mid = (low + high) // 2
            if self.hours_taken(piles, mid) <= h:
                # print(mid, eating_rate)
                eating_rate = min(mid, eating_rate)
                high = mid - 1
            else:
                low = mid + 1
        
        return eating_rate



    def hours_taken(self, piles, k):
        total_hours = 0
        for pile in piles:
            hours = pile // k
            hours = hours + 1 if (pile % k) else hours
            total_hours += hours
        # print(total_hours)
        return total_hours
