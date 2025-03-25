from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            key = ''.join(sorted(word)) 
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)

        return list(anagrams.values())

solution = Solution()

# Test 1: Basic case
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Expected: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

# Test 2: Single string
print(solution.groupAnagrams(["hello"]))
# Expected: [["hello"]]

# Test 3: Empty list
print(solution.groupAnagrams([]))
# Expected: []
