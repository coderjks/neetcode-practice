class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        cur_sum = 0
        threshold *= k

        for R in range(len(arr)):
            cur_sum += arr[R]
            if R >= k - 1:
                print(cur_sum, threshold)
                if cur_sum >= threshold:
                    count += 1
                cur_sum -= arr[R - k + 1]  
            
        return count