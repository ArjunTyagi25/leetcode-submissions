class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        


        dict_set = set(dictionary)
        max_dict_len = float('-inf')
        for dict_word in dict_set:
            max_dict_len = max(max_dict_len, len(dict_word))
        words = sentence.split()
        res = []

        for word in words:
            isAppended = False
            for i in range(min(max_dict_len, len(word))):
                if word[:i+1] in dict_set:
                    res.append(word[:i+1])
                    isAppended = True
                    break

            if not isAppended:
                res.append(word)

        return " ".join(res)


'''
            -1
       "c"  "b"    "r"
    "a"
  "t"
"t"



'''
            
                


        