class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        best = 0
        counter = 0
        sort = sorted(nums)
        past = sort[0]
        for i in range(1,len(nums)):
            if past == sort[i]:
                continue
            
            if (past + 1) == sort[i]:
                counter += 1
            else: counter = 0 
            if counter > best: 
                best = counter
            past = sort[i]

        
        return best + 1
