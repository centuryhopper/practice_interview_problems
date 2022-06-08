/*
["WordDictionary","addWord","addWord","search","search","search","search","search","search"]
[[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]]

["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
[[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]
*/


class TrieNode
{
    isEnd:boolean;
    m: any;
    constructor()
    {
        this.isEnd = false
        this.m = {}
    }
}


class WordDictionary
{
    root:TrieNode;
    constructor()
    {
        this.root = new TrieNode()
    }


    addWord(word: string): void
    {
        var tmp = this.root
        for (const w of word)
        {
            if (!tmp.m[w])
            {
                 tmp.m[w] = new TrieNode();
            }

            tmp = tmp.m[w]
        }

        tmp.isEnd = true
    }

    search(word: string): boolean
    {
        function rec(word: string, i:number, trieNode: TrieNode): boolean
        {
            if (i == word.length) return trieNode.isEnd
            if (word[i] != '.' && !trieNode.m[word[i]]) return false

            // wildcard
            if (word[i] == '.')
            {
                // try every key in the map
                for (const c in trieNode.m)
                {
                    if (rec(word,i+1,trieNode.m[c])) return true
                }

                return false
            }
            else
            {
                return rec(word,i+1,trieNode.m[word[i]])
            }

        }

        return rec(word,0,this.root)
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */