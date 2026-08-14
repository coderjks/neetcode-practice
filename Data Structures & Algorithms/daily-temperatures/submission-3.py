class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        temp_stack = [n-1]
        # last day will always be zero
        result = [0] * n

        for i in range(n - 2, -1, -1):
            while temp_stack and temperatures[i] >= temperatures[temp_stack[-1]]:
                temp_stack.pop()
            days_diff = 0
            if temp_stack:
                days_diff = temp_stack[-1] - i
            temp_stack.append(i)
            # because we iterating backware temp_stack will always have higher idx
            
            result[i] = days_diff
        
        return result