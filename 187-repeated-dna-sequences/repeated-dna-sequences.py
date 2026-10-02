class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        if len(s) < 10:
            return []

        seen_sequences = set()
        res = set()

        for i in range(len(s) - 9):
            window = s[i:i+10]
            
            if window in seen_sequences:
                res.add(window)
            else:
                seen_sequences.add(window)

        
        return list(res)