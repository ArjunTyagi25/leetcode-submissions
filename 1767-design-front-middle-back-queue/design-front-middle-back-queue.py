class Node:
    def __init__(self, val = -1, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class FrontMiddleBackQueue:
    def __init__(self):
        self.Front, self.Back = Node(-1), Node(-1)
        self.Front.prev, self.Back.next = self.Back, self.Front
        self.count = 0
        self.middleNode = None

    def pushFront(self, val: int) -> None:
        node = Node(val)
        currFront = self.Front.prev

        # Update currFront and node to point to each other
        currFront.next, node.prev = node, currFront

        # Update Front and node to point to each other
        node.next, self.Front.prev = self.Front, node

        self.count += 1
        if self.middleNode:
            if self.count % 2 == 0:
                self.middleNode = self.middleNode.next
        else:
            self.middleNode = node

    def pushMiddle(self, val: int) -> None:
        node = Node(val)

        # Current length is odd
        if self.count % 2 != 0:
            leftOfMiddle = self.middleNode.next

            # Update middleNode and node to point to each other
            self.middleNode.next, node.prev = node, self.middleNode

            # Update node and leftOfMiddle to point to each other
            node.next, leftOfMiddle.prev = leftOfMiddle, node

            self.middleNode = node
            self.count += 1
        else:
            if self.count == 0:
                self.pushFront(val)
            else:
                rightOfMiddle = self.middleNode.prev

                # Update rightOfMiddle and node to point to each other
                rightOfMiddle.next, node.prev = node, rightOfMiddle

                # Update node and middleNode to point to each other
                node.next, self.middleNode.prev = self.middleNode, node

                self.middleNode = node

                self.count += 1
        

    def pushBack(self, val: int) -> None:
        node = Node(val)
        currBack = self.Back.next

        # Update currBack and node to point to each other
        currBack.prev, node.next = node, currBack

        # Update Back and node to point to each other
        node.prev, self.Back.next = self.Back, node

        self.count += 1
        if self.middleNode:
            if self.count % 2 != 0:
                self.middleNode = self.middleNode.prev
        else:
            self.middleNode = node

    def popFront(self) -> int:
        if self.count == 0:
            return -1

        frontNode = self.Front.prev
        rightOfFrontNode = frontNode.prev

        # Update Front and rightOfFrontNode to point to each other
        self.Front.prev, rightOfFrontNode.next = rightOfFrontNode, self.Front

        if self.count % 2 == 0:
            self.middleNode = self.middleNode.prev

        self.count -= 1
        if self.count == 0:
            self.middleNode = None

        return frontNode.val
        

    def popMiddle(self) -> int:
        if self.count == 0:
            return -1

        leftOfMiddle = self.middleNode.next
        rightOfMiddle = self.middleNode.prev

        leftOfMiddle.prev, rightOfMiddle.next = rightOfMiddle, leftOfMiddle
        val = self.middleNode.val

        if self.count % 2 == 0:
            self.middleNode = rightOfMiddle
        else:
            self.middleNode = leftOfMiddle

        self.count -= 1
        if self.count == 0:
            self.middleNode = None
        return val

    def popBack(self) -> int:
        if self.count == 0:
            return -1

        backNode = self.Back.next
        leftOfBackNode = backNode.next

        # Update Back and leftOfBackNode to point to each other
        self.Back.next, leftOfBackNode.prev = leftOfBackNode, self.Back

        if self.count % 2 != 0:
            self.middleNode = self.middleNode.next

        self.count -= 1
        if self.count == 0:
            self.middleNode = None

        return backNode.val
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()