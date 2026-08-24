class TrieNode:

    def __init__(self):
        self.char_map = dict()
        self.isEnd = False
    
    def getChar(self, ch):
        return self.char_map.get(ch, None)
    
    def putChar(self, ch):
        self.char_map[ch] = TrieNode()
    
    def isEndOfWord(self):
        return self.isEnd
    
    def setEndOfWord(self, val = False):
        self.isEnd = val

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur_node = self.root
        for ch in word:
            if not cur_node.getChar(ch):
                cur_node.putChar(ch)
            cur_node = cur_node.getChar(ch)
        cur_node.setEndOfWord(True)


    def search(self, word: str) -> bool:
        cur_node = self.root
        for ch in word:
            if not cur_node:
                return False
            cur_node = cur_node.getChar(ch)
        
        return cur_node.isEndOfWord() if cur_node else False


    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for ch in prefix:
            if not cur_node:
                return False
            cur_node = cur_node.getChar(ch)
            
        return True if cur_node else False
        
        