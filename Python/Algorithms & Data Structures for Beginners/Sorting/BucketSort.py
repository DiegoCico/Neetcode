class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = [0,0,0]
        for i in nums:
            arr[i] += 1
        print(arr)

        a = 0
        for i in range(len(arr)):
            for j in range(arr[i]):
                nums[a] = i
                a += 1

        