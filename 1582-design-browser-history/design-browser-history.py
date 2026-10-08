class Node:
    def __init__(self, val = "", next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.Homepage = Node(homepage)
        self.currentWebsite = self.Homepage
        self.lenToHomepage = 0
        

    def visit(self, url: str) -> None:
        node = Node(url)

        self.currentWebsite.next, node.prev = node, self.currentWebsite
        self.currentWebsite = node
        self.lenToHomepage += 1
        

    def back(self, steps: int) -> str:
        if steps >= self.lenToHomepage:
            self.currentWebsite = self.Homepage
            self.lenToHomepage = 0
            return self.Homepage.val

        count = 0
        while count < steps:
            self.currentWebsite = self.currentWebsite.prev
            count += 1
            self.lenToHomepage -= 1

        return self.currentWebsite.val

    def forward(self, steps: int) -> str:
        count = 0

        while count < steps and self.currentWebsite.next:
            self.currentWebsite = self.currentWebsite.next
            count += 1
            self.lenToHomepage += 1

        return self.currentWebsite.val

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)