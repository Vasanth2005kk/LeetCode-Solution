class RLEIterator:

    def __init__(self, encoding: list[int]):
        self.decodeValue = self.decode(encoding)
        print('Decode Values : ',self.decodeValue)
        self.index = 0


    def decode(self,encodearr):
        length = len(encodearr) // 2
        left = 0
        right = 1

        decode = []
        for _ in range(length):
            decode.extend([encodearr[right]] * encodearr[left])
            left += 2 
            right += 2

        return decode


    def next(self, n: int) -> int:
        if self.decodeValue:
            ans = self.decodeValue[0:n]
            if len(ans) == n:
                self.decodeValue = self.decodeValue[n:]
                return ans[-1]
            self.decodeValue = self.decodeValue[n:]
            return -1



# Your RLEIterator object will be instantiated and called as such:
encoding = [3,8,2,5]
encoding = [3,8,0,9,2,5]
encoding = [2,8,1,8,2,5]

obj = RLEIterator(encoding)

obj.next(2)
obj.next(1)
obj.next(1)
obj.next(2)


"""
class RLEIterator:

    def __init__(self, encoding: list[int]):
        self.encoding = encoding
        self.index = 0

    def next(self, n: int) -> int:

        while self.index < len(self.encoding):

            count = self.encoding[self.index]
            value = self.encoding[self.index + 1]

            if count >= n:
                self.encoding[self.index] -= n
                return value

            n -= count
            self.index += 2

        return -1
"""
