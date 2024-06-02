class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        return longUrl
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return shortUrl
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

# import secrets
# import string
# key_characters = string.ascii_letters + string.digits
# class Codec:
#     mapping = {}
#     def encode(self, longUrl: str) -> str:
#         random_key = ''.join(secrets.choice(key_characters) for _ in range(6))
#         self.mapping[random_key] = longUrl
#         return random_key
        

#     def decode(self, shortUrl: str) -> str:
#         """Decodes a shortened URL to its original URL.
#         """
#         return self.mapping[shortUrl]
        

# # Your Codec object will be instantiated and called as such:
# # codec = Codec()
# # codec.decode(codec.encode(url))