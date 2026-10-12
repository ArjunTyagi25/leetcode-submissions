class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        rle_str = self.countAndSay(n - 1)
        return self.RLE(rle_str)
        

    def RLE(self, string):
        res = []
        i = 0

        while i < len(string):
            count = 1
            while i < len(string) - 1 and string[i] == string[i+1]:
                count += 1
                i += 1
            
            res.append(str(count))
            res.append(string[i])
            i += 1

        return "".join(res)