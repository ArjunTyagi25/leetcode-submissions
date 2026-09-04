class Solution:
    def calculate(self, s: str) -> int:
        if len(s) == 1:
            return int(s)

        queue = deque()
        num_str = ""
        for i in range(len(s)):
            if s[i] in ["+", "-", "*", "/"]:
                if queue and queue[-1] == "*":
                    num2 = int(num_str)
                    queue.pop()
                    num1 = int(queue[-1])
                    queue.pop()
                    queue.append(str(num1 * num2))
                elif queue and queue[-1] == "/":
                    num2 = int(num_str)
                    queue.pop()
                    num1 = int(queue[-1])
                    queue.pop()
                    queue.append(str(num1//num2))
                else:
                    queue.append(num_str)
                
                num_str = ""
                queue.append(s[i])
            elif s[i] == " ":
                continue
            else:
                num_str += s[i]

        if num_str != "":
            if queue and queue[-1] == "*":
                num2 = int(num_str)
                queue.pop()
                num1 = int(queue[-1])
                queue.pop()
                queue.append(str(num1 * num2))
            elif queue and queue[-1] == "/":
                num2 = int(num_str)
                queue.pop()
                num1 = int(queue[-1])
                queue.pop()
                queue.append(str(num1//num2))
            else:
                queue.append(num_str)

        print(queue)
        while len(queue) != 1:
            num1 = int(queue.popleft())
            op = queue.popleft()
            num2 = int(queue.popleft())
        
            if op == "+":
                queue.appendleft(str(num1 + num2))
            elif op == "-":
                queue.appendleft(str(num1 - num2))
        
        return int(queue[0])