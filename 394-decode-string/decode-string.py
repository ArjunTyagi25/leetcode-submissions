class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if stack == [] or s[i] != "]":
                stack.append(s[i])
            else:
                string = ""
                while stack and stack[-1] != "[":
                    string += stack[-1]
                    stack.pop()
                
                string = string[::-1]
                # Pop the "["
                stack.pop()
                number = ""
                while stack and stack[-1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    number += stack[-1]
                    stack.pop()

                number = int(number[::-1])
                string = string * number
                for t in string:
                    stack.append(t)
        
        return "".join(stack)