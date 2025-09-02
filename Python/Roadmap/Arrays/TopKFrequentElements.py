class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        
        sorted_items = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]