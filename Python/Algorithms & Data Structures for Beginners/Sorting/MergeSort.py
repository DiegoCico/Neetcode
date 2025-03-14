# O(nLogn)

# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
       l = self.divide(pairs, 0, len(pairs))
       return l

    def divide(self, arr: List[Pair], start: int, end:int) -> List[Pair]:
        if end - start + 1 <= 1:
            return arr

        middle = (start+end) // 2
        #left bound
        self.divide(arr, 0, middle)

        #right bound
        self.divide(arr, middle+1, end)

        self.merge(arr, start, middle + 1, end)

        return arr

    def merge(self, arr, start, middle, end): 
        L = arr[start : middle]
        R = arr[middle : end+1]

        i = 0 # pointer for L
        j = 0 # pointer for R
        k = start # index for arr

        # Merge the two sorted halfs into the original array
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
