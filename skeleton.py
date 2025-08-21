class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TextEditor:
    def __init__(self):
        self.head = Node("Head")
        self.tail = Node("Tail")
        self.cursor = Node("Cursor")
        self.head.right = self.cursor
        self.cursor.left = self.head
        self.cursor.right = self.tail
        self.tail.left = self.cursor

    def addText(self, text: str) -> None:
        prev = self.cursor.left
        for char in text:
            new_node = Node(char, prev, self.cursor)
            prev.right = new_node
            self.cursor.left = new_node
            prev = new_node

    def deleteText(self, k: int) -> int:
        count = 0
        curr = self.cursor.left
        while curr != self.head and count < k:
            prev = curr.left
            prev.right = self.cursor
            self.cursor.left = prev
            curr.left = curr.right = None  # help GC
            curr = prev
            count += 1
        return count

    def _get_last_10_chars(self) -> str:
        res = []
        curr = self.cursor.left
        for _ in range(10):
            if curr == self.head:
                break
            res.append(curr.val)
            curr = curr.left
        return ''.join(reversed(res))

    def cursorLeft(self, k: int) -> str:
        for _ in range(k):
            if self.cursor.left == self.head:
                break
            left_node = self.cursor.left
            right_node = self.cursor.right
            # Swap cursor with left_node
            left_left = left_node.left

            # Relink nodes
            left_left.right = self.cursor
            self.cursor.left = left_left
            self.cursor.right = left_node
            left_node.left = self.cursor
            left_node.right = right_node
            right_node.left = left_node
        return self._get_last_10_chars()

    def cursorRight(self, k: int) -> str:
        for _ in range(k):
            if self.cursor.right == self.tail:
                break
            right_node = self.cursor.right
            left_node = self.cursor.left
            # Swap cursor with right_node
            right_right = right_node.right

            # Relink nodes
            left_node.right = right_node
            right_node.left = left_node
            right_node.right = self.cursor
            self.cursor.left = right_node
            self.cursor.right = right_right
            right_right.left = self.cursor
        return self._get_last_10_chars()
