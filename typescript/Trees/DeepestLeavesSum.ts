class TreeNode
{
    public val: number;
    public left: TreeNode;
    public right: TreeNode;

    constructor(val: number, left: TreeNode, right: TreeNode)
    {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}

 var deepestLeavesSum = function(root: TreeNode)
 {
     if (root === null) return 0;
     // function to get the height of any tree
     const ht = (root: TreeNode): number =>
     {
         // assume a null tree has a height of -1
         if (root === null) return -1
         return 1 + Math.max(ht(root.left), ht(root.right))
     }
     const height : number = ht(root)

     let q : TreeNode[] = [root,null]
     let ans : number = 0
     let level : number = 0
     while (true)
     {
        //  remove first element of queue
         const cur : TreeNode = q.shift()
         if (cur === null)
         {
            //  break out of loop when there are no more nodes left
             if (q.length === 0)
                 break
            // prepare a null node for the next level
             q.push(null)
             // we know we must be traversing the next level of nodes at this point
             level++
         }
         else
         {
             if (level === height)
             {
                 ans += cur.val
             }
             if (cur.left !== null) q.push(cur.left)
             if (cur.right !== null) q.push(cur.right)
         }
     }

     return ans

 };