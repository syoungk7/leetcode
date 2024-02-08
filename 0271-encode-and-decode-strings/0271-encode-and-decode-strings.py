class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encode_lst = []
        k = 27
        for word in strs:
            tmp = []
            for char in word:
                tmp.append(ord(char)+k)
            encode_lst.append(tmp)
        return encode_lst

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decode_lst = []
        k = 27
        for word in s:
            tmp = []
            for char in word:
                tmp.append(chr(char-k))
            decode_lst.append(''.join(tmp))
        return decode_lst
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))