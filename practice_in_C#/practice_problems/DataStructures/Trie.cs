using System.Text.RegularExpressions;
using System;
using System.Collections.Generic;

namespace data_structures
{
    /// <summary>
    /// a Trie data structure with case insensitive comparisons
    /// Only alphabetical letters should be inputted into the trie
    /// </summary>
    public class Trie
    {
        private class TrieNode
        {
            // whether this is the end of the word or not
            public bool isEndOfWord { get; set; }

            /// <summary>
            /// should contain upper-case characters only
            /// </summary>
            public Dictionary<char, TrieNode> children { get; private set; }

            public TrieNode()
            {
                isEndOfWord = false;
                children = new Dictionary<char, TrieNode>();
            }

            public TrieNode(Dictionary<char, TrieNode> dict)
            {
                isEndOfWord = false;
                children = dict;
            }
        }

        private TrieNode root;

        public Trie() { root = new TrieNode(); }

        private void p(object m) => Console.WriteLine(m);

        /// <summary>
        /// iteratively inserts a word into the trie data
        /// structure and marks the node that the last character of
        /// the word points at to true
        /// Time complexity: O(l), where l is the length of the string
        /// </summary>
        /// <param name="word">The word to insert</param>
        public void InsertWord(string word)
        {
            if (word.Equals(String.Empty)) { return; }

            if (!IsAValidWord(word))
            {
                p("this word is invalid. Please make sure all the characters in your word are letters in the alphabet");
                return;
            }

            TrieNode tmp = root;

            for (int i = 0; i < word.Length; ++i)
            {
                // check whether the character
                // is already in the hashmap or not
                if (!tmp.children.ContainsKey(word[i]))
                {
                    tmp.children.Add(word[i], new TrieNode());
                    tmp = tmp.children[word[i]];
                }
                else
                {
                    tmp = tmp.children[word[i]];
                }
            }

            // to signal that we have entered a whole/complete word
            tmp.isEndOfWord = true;
        }

        /// <summary>
        /// error checking method
        /// Time complexity: O(l), where l is the length of the string
        /// </summary>
        /// <returns>whether the input word is valid or not</returns>
        public bool IsAValidWord(string word)
        {
            // strip word of all spaces
            word = Regex.Replace(word, @"\s+", "").ToUpper();
            return Array.TrueForAll<char>(word.ToCharArray(), letter => Char.IsLetter(letter));
        }

        /// <summary>
        /// Searchs for for the input.
        /// Note that it must be a complete word in the trie,
        /// and NOT a prefix or it will not find it
        /// Time complexity: O(l), where l is the length of the string
        /// </summary>
        /// <param name="word">The complete word to find</param>
        /// <returns>whether or not the input was found</returns>
        public bool Contains(string word)
        {
            if (word.Length == 0) { return true; }

            if (!IsAValidWord(word))
            {
                p("this word is invalid. Please make sure all the characters in your word are letters in the alphabet");
            }

            TrieNode tmp = root;

            for (int i = 0; i < word.Length; ++i)
            {
                if (!tmp.children.ContainsKey(word[i])) { return false; }

                tmp = tmp.children[word[i]];
            }

            return tmp.isEndOfWord;
        }

        /// <summary>
        /// Searchs for the prefix an inserted word
        /// It works also on complete words as well
        /// Time complexity: O(l), where l is the length of the string
        /// </summary>
        /// <param name="prefix">The prefix word to find</param>
        /// <returns>Whether or not the prefix was found</returns>
        public bool StartsWith(string prefix)
        {
            if (prefix.Length == 0) { return true; }

            if (!IsAValidWord(prefix))
            {
                p("this word is invalid. Please make sure all the characters in your word are letters in the alphabet");
            }

            TrieNode tmp = root;

            for (int i = 0; i < prefix.Length; ++i)
            {
                if (!tmp.children.ContainsKey(prefix[i])) { return false; }

                tmp = tmp.children[prefix[i]];
            }

            return true;
        }

        /// <summary>
        /// Removes the input word from the trie data structure,
        /// if it exists.
        /// Time complexity: O(l), where l is the length of the string
        /// </summary>
        /// <param name="word">The word to remove</param>
        public void DeleteWord(string word)
        {

        }

    }
}



