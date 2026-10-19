class TextEditor:

    def __init__(self):
        self.left = []
        self.right = []

    def addText(self, text: str) -> None:
        self.left.extend(text)

    def deleteText(self, k: int) -> int:
        deleted = min(k, len(self.left))

        for _ in range(deleted):
            self.left.pop()

        return deleted

    def cursorLeft(self, k: int) -> str:
        for _ in range(min(k, len(self.left))):
            self.right.append(self.left.pop())

        return ''.join(self.left[-10:])

    def cursorRight(self, k: int) -> str:
        for _ in range(min(k, len(self.right))):
            self.left.append(self.right.pop())

        return ''.join(self.left[-10:])



# Test
obj = TextEditor()
obj.addText("leetcode")
print(obj.deleteText(4))
obj.addText("practice")
print(obj.cursorRight(3))
print(obj.cursorLeft(8))
print(obj.deleteText(10))
print(obj.cursorLeft(2))
print(obj.cursorRight(6))