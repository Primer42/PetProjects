'''
Created on Oct 20, 2013

@author: will

See what strings of words we can create using one (or 2 or 3)
of each letter of the alphabet
'''
import sys
from collections import defaultdict, Counter


class Trie:
    def __init__(self):
        self.root = defaultdict(Trie)
        self.value = None

    def add(self, s):
        head, tail = s[0], s[1:]
        cur_node = self.root[head]
        if not tail:
            cur_node.value = s
        cur_node.add(tail)

    def lookup(self, s):
        head, tail = s[0], s[1:]
        node = self.root[head]
        if tail:
            node.lookup(tail)
        else:
            return node.value

    def remove(self, s):
        head, tail = s[0], s[1:]
        if head not in self.root:
            return False
        node = self.root[head]
        if tail:
            return node.remove(tail)
        else:
            del node
            return True

    def isPrefix(self, p):
        if not p:
            return True
        head, tail = p[0], p[1:]
        if head in self.root():
            return self.root[head].isPrefix(tail)
        else:
            return False


def getKey(s):
    return ''.join(sorted(s))

if __name__ == '__main__':
    #load our dictionary
    allWords = [w.strip() for w in open('./dictionary.txt', 'r')]
    #our one argument is the number of duplicate letters we allow
    numRepeatedLetters = int(sys.argv[1])
    #start by removing words from our dictionary that have a letter repeated
    #more than 'numRepeatedLetters' times, because they clearly
    #cannot be in the solution
    validWords = [w for w in allWords
                  if Counter(w).most_common(1)[0][1] <= numRepeatedLetters]
    #keep things clean
    del allWords
    #put them into the Trie
    #trie = Trie()
    #[trie.add(w) for w in validWords]
    #del validWords
    wordDict = defaultdict(list)
    for w in validWords:
        wordDict[getKey(w)].append(w)
    print wordDict
    
    