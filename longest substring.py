class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        watched = []

        st = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in st:
                st.remove(s[l])
                l+=1
            st.add(s[r])
            res = max(res, r - l + 1)
        print(st)
        return res
        # c = 0
        # for idx, el in enumerate(s):
        #     if c >= 1:
        #         before_el = s[idx - 1]
        #         if before_el != el:
        #             if el not in watched:
        #                 watched.append(before_el)
        #         else:
        #             watched.clear()
        #     c += 1
            # if el not in watched:
            #     watched.append(el)


obj = Solution()
print(obj.lengthOfLongestSubstring("pwwkew"))
