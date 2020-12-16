using data_structures;

namespace practice_problems
{
    public class SymmetricTree
    {
        private bool helper(TreeNode l, TreeNode r)
        {
            if (l == null && r == null) { return true; }
            if (l == null || r == null) { return false; }
            if (l.val != r.val) { return false; }

            return helper(l.left, r.right) &&
                   helper(l.right, r.left);
        }

        // recursive method
        public bool IsSymmetric(TreeNode root)
        {
            return root == null || helper(root.left, root.right);
        }
    }
}