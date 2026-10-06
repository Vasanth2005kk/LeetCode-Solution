class Codec:

    def __init__(self):
        self.urls = {}
        self.count = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""

        self.count += 1
        shortUrl = str(self.count)
        self.urls[shortUrl] = longUrl

        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to the original URL."""
        return self.urls[shortUrl]


# Your Codec object will be instantiated and called as such:
codec = Codec()

url = "https://leetcode.com/problems/design-tinyurl"

short = codec.encode(url)
print(short)

original = codec.decode(short)
print(original)