
class TextEditor:

    def __init__(self):
        self.cursor = 0
        self.content = ""

    def addText(self, text: str) -> None:
        self.content = (
            self.content[:self.cursor]
            + text
            + self.content[self.cursor:]
        )
        self.cursor += len(text)

    def deleteText(self, k: int) -> int:
        k = min(k, self.cursor)

        self.content = (
            self.content[:self.cursor - k]
            + self.content[self.cursor:]
        )

        self.cursor -= k
        return k

    def cursorLeft(self, k: int) -> str:
        self.cursor = max(0, self.cursor - k)

        return self.content[max(0, self.cursor - 10):self.cursor]

    def cursorRight(self, k: int) -> str:
        self.cursor = min(len(self.content), self.cursor + k)

        return self.content[max(0, self.cursor - 10):self.cursor]


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