class Trie:
    def __init__(self):
        self.trie = {}
    def insert(self, word:str) -> None:
        node = self.trie
        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]
        node["$"] = True # mark the end of the string
    def search(self, word:str) -> bool:
        node = self.trie
        for ch in word:
            if not ch in node:
                return False
            else:
                node = node[ch]
        return "$" in node

    def startswith(self, prefix:str) -> bool:
        node = self.trie
        for ch in prefix:
            if not ch in node:
                return False
            else:
                node = node[ch]
        return True