class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""
        result = ""
        base = strs[0]
        
        for i in range(0, len(base)):
            for word in strs[1:]:
                if  i == len(word) or word[i] != base[i]:
                    return result
        
            result += base[i]
        return result

strs = ["flower","flow","flight"]
sol = Solution()
print(sol.longestCommonPrefix(strs))  # Output: "fl"

