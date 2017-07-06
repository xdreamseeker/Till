import collections
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.childNode = collections.defaultdict(TrieNode)
        self.isEnd = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        length = len(word)
        p = self.root
        for c in word:
            p = p.childNode[c]
        p.isEnd = True



    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self.root
        for c in word:
            p = p.childNode.get(c)
            if p is None:
                return False
        return p.isEnd



    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self.root
        for c in prefix:
            p = p.childNode.get(c)
            if p is None:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
if __name__=="__main__":
    trie = Trie()
    trie.insert("somestring")
    trie.insert("abc")
    trie.insert("abcdef")
    trie.insert("ab")
    print(trie.search("abc"))
    print(trie.startsWith("a"))
    print(trie.startsWith("b"))


