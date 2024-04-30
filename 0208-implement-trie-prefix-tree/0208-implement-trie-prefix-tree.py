
class Trie:
    def __init__(self):
        self.dic = {}

    def insert(self, word: str) -> None:
        self.dic[word] = True

    def search(self, word: str) -> bool:
        if word in self.dic:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        l = len(prefix)
        for k, v in self.dic.items():
            if prefix == k[:l]:
                return True
        return False