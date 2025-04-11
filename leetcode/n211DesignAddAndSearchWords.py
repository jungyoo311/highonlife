class WordDictionary:

    def __init__(self):
        self.trie = {}
    def addWord(self, word: str) -> None:
        node = self.trie
        for ch in word:
            if not ch in node:
                node[ch] = {}
            # recursively assign new nodes.
            node = node[ch]
        # represents it reached to the end of the node.
        node["$"] = True

    def search(self, word: str) -> bool:
        def search_in_node(word, node) -> bool:
            for i, ch in enumerate(word):
                if not ch in node:
                    if ch == ".":
                        for x in node:
                            if x != "$" and search_in_node(word[i + 1:], node[x]):
                                return True
                    return False
                else:
                    node = node[ch]
            return "$" in node
        return search_in_node(word, self.trie)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)