    class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                needed = self.needed_num(nums[i], nums[j])
                summ = nums[i] + nums[j] + needed
                n_count = nums.count(needed)
                if needed in nums and summ == 0 and self.has_space([nums[i],nums[j]], needed, n_count):
                    results.add(tuple(sorted([nums[i], nums[j], needed])))

        return [list(triplet) for triplet in results]

    def needed_num(self, num1, num2):
        return -(num1 + num2)

    def has_space(self, nums, need, count): 
        if nums[0] == need:
            count -= 1
        if nums[1] == need:
            count -= 1
        if need in nums and count <= 0:
            return False
        return True
