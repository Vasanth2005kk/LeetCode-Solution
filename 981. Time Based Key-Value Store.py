class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []

        self.dic[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""

        arr = self.dic[key]

        left = 0
        right = len(arr) - 1

        result = ""

        while left <= right:
            mid = (left + right) // 2

            if arr[mid][0] <= timestamp:
                result = arr[mid][1]
                left = mid + 1

            else:
                right = mid - 1

        return result


# Your TimeMap object will be instantiated and called as such:

# Input

# ["TimeMap","set","set","get","get","get","get","get"]
# [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]

# Output

# [null,null,null,"","high","high","low","low"]



obj = TimeMap()
print("None")
obj.set("love","high",10)
obj.set("love","low",20)

obj.get("love",5)
obj.get("love",10)
obj.get("love",15)
obj.get("love",20)
obj.get("love",25)



