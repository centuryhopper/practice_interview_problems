
class Codec:

    def __init__(self):
        self.cache = []

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.cache.append(longUrl)
        return str(len(self.cache) - 1)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.cache[int(shortUrl)]














# optimized online solution
# import random

# class Codec:
#     def __init__(self):
#         self.db = {}
#         self.prefix = "http://tinyurl.com/"

#     def encode(self, longUrl: str) -> str:
#         """Encodes a URL to a shortened URL.
#         """
#         aux = longUrl.split("/")
#         coded = str(len(aux))
#         for s in aux:
#             if len(s) > 0:
#                 coded += s[0]
#         #may: 65-90
#         #min: 97-122

#         while coded in self.db:
#             rand = chr(random.randint(65,90))
#             coded += rand

#         self.db[coded] = longUrl
#         return self.prefix + coded


#     def decode(self, shortUrl: str) -> str:
#         """Decodes a shortened URL to its original URL.
#         """
#         key = shortUrl.split("/")[-1]
#         if key in self.db:
#             return self.db[key]

