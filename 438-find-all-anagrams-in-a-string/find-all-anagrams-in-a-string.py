class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        p_freq = [0] * 26
        for c in p:
            p_freq[ord(c) - ord('a')] += 1

        window_freq = [0] * 26
        for i in range(len(p)):
            window_freq[ord(s[i]) - ord('a')] += 1

        res = [] if window_freq != p_freq else [0]

        for i in range(0, len(s) - len(p)):
            window_freq[ord(s[i]) - ord('a')] -= 1
            window_freq[ord(s[i + len(p)]) - ord('a')] += 1
            if window_freq == p_freq:
                res.append(i+1)

        return res

'''
s = cdeghab => len(s) = 7
p = abc => len(p) = 3

'''
        