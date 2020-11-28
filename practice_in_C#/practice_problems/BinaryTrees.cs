using System;
using data_structures;

public class BinaryTrees
{
    // example
    // 1   2
    //    /
    //   3

    private void print(object msg) => Console.WriteLine(msg);

    public TreeNode MergeTrees(TreeNode t1, TreeNode t2)
    {
        if (t1 == null && t2 == null) { return null; }
        if (t1 == null) { return t2; }
        if (t2 == null) { return t1; }

        // both are not null. Best to not create a brand new tree with copies
        // and use existing given trees (respect runtime and space complexity)
        t1.val += t2.val;

        // recurse left and right
        t1.left = MergeTrees(t1.left, t2.left);
        t1.right = MergeTrees(t1.right, t2.right);
        
        return t1;
    }
}

