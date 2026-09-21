class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # n = len(nums)
        # left, right = 0, n - 1
        # target = newInterval[1]

        # while left <= right:
        #     mid = (left + right) // 2
        #     if intervals[mid][0] < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        
        # intervals.insert(left, newInterval)

        res = []
        # for interval in intervals:
        #     if not res or res[-1][1] < interval[0]:
        #         res.append(interval)
        #     else:
        #         res[-1][1] = max(res[-1][1], interval[1])
        
        # return res

        # Greedy solution
        for i in range(len(intervals)):

            interval = intervals[i]
            # check if no conflict
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > interval[1]:
                res.append(intervals[i])
            else:
                # merge if conflict
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
        
        res.append(newInterval)
        return res

