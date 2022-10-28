'''
/**
 * Date 10/10/2022
 * @author Leo
 * adapted from tuschar roy's implementation
 *
 * Construct suffix tree using Ukkonen's algorithm
 *
 * Solution
 * Rule 1: For phase i+1 if S[j..i] ends at last character of leaf edge then add S[i+1] at
 * the end.
 * Rule 2: For phase i+1 if S[j..i] ends somewhere in middle of edge and next character is
 * not S[i+1] then a new leaf edge with label S[i+1] should be created
 * Rule 3: For phase i+1 if S[j..i] ends somewhere in middle of edge and next character is
 * S[i+1] then do nothing(resulting in implicit tree)
 *
 * Suffix Link:
 * For every node with label x@ where x is a single character and @ is possibly empty substring
 * there is another node with label x. This node is suffix link of first node. If @ is
 * empty then suffix link is root.
 *
 * Trick1
 * Skip/Count trick
 * While traveling down if number of characters on edge is less than number of characters
 * to traverse then skip directly to the end of the edge. If number of characters on label
 * is more than number of characters to traverse then go directly to that character
 * we care about.
 *
 * Edge-label compression
 * Instead of storing actual characters on the path store start and end indices on the
 * path.
 *
 * Trick2 - Stop process as soon as you hit rule 3. Rule 3 is show stopper
 *
 * Trick3 - Keep a global end on leaf to do rule 1 extension.
 *
 * Active point - It is the point from which traversal starts for next extension or next phase.
 * Active point always starts from root. Other extension will get active point set up
 * correctly by last extension.
 *
 * Active node - Node from which active point will start
 * Active Edge - It is used to choose the edge from active node. It has index of character.
 * Active Length - How far to go on active edge.
 *
 * Active point rules
 * 1) If rule 3 extension is applied then active length will increment by 1 if active length is not greater then length of path on edge.
 * 2) If rule 3 extension is applied and if active length gets greater than length path of edge then change active node, active edge and active length
 * 3) If active length is 0 then always start looking for the character from root.
 * 4) If rule 2 extension is applied and if active node is root then active edge is active edge + 1 and active length is active lenght -1
 * 5) If rule 2 extension is applied and if active node is not root then follow suffix link and make active node as suffix link and do no change
 * anything.
 *
 * Test cases
 * adeacdade
 * abcabxabcd
 * abcdefabxybcdmnabcdex
 * abcadak
 * dedododeodo
 * abcabxabcd
 * mississippi
 * banana
 * ooooooooo
 *
 * References
 * http://web.stanford.edu/~mjkay/gusfield.pdf
 * http://www.geeksforgeeks.org/ukkonens-suffix-tree-construction-part-6/
 * https://www.cs.helsinki.fi/u/ukkonen/SuffixT1withFigs.pdf
 * https://gist.github.com/axefrog/2373868
 */

'''

from re import T


class SuffixNode:
    TOTAL=256
    def __init__(self):
        self.child = [SuffixNode() for _ in range(SuffixNode.TOTAL)]
        self.start=-1
        self.end : End = None
        self.index=-1
        self.suffixLink : SuffixNode = None

    @staticmethod
    def createNode(start:int,end:int):
        node = SuffixNode()
        node.start = start
        node.end = end
        return node
    def __str__(self) -> str:
        i = 0
        buffer = []
        for node in self.child:
            if node:
                buffer.append(chr(i))
            i+=1
        return f'SuffixNode [start={self.start}] {" ".join(buffer)}'



class End:
    def __init__(self, end:int=-1):
        self.end = end
class Active:
    def __init__(self, node:SuffixNode):
        self.activeLength = 0
        self.activeNode = node
        self.activeEdge = -1

    def __str__(self) -> str:
        return f'Active [activeNode={self.activeNode},activeIndex={self.activeEdge}, activeLength={self.activeLength}]'

class SuffixTree:
    def __init__(self):
        pass







if __name__ == '__main__':
    pass
    # st = SuffixTree('mississippi')
    # st.build()
    # st.dfsTraversal()
    # print(st.validate())

