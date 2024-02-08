class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encode_lst = []
        k = 27
        for word in strs:
            tmp = []
            for char in word:
                tmp.append(str(ord(char)+k))
                tmp.append('//')
            encode_lst.append(''.join(tmp))
            encode_lst.append('|//|')
        return ''.join(encode_lst)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        print(s)
        decode_lst = []
        k = 27


        for word in s.split('|//|')[0:len(s.split('|//|'))-1]:
            tmp = []
            # if word:
            for char in word.split('//'):
                if char:
                    tmp.append(chr(int(char)-k))
            decode_lst.append(''.join(tmp))
        return decode_lst
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))