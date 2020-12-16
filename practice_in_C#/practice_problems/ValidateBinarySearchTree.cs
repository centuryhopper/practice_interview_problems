using data_structures;

namespace practice_problems
{
    public class ValidateBinarySearchTree
    {
        private bool helper(TreeNode root, long min, long max)
        {
            // makes sure leaf nodes return true
            if (root == null) { return true; }

            // must be within range
            if (root.val <= min || root.val >= max)
            {
                return false;
            }

            bool flag = true;

            flag &= helper(root.left, min, root.val);
            flag &= helper(root.right, root.val, max);

            return flag;
        }

        public bool IsValidBST(TreeNode root)
        {
            // empty tree
            if (root == null) { return true; }

            return helper(root.left, (long)int.MinValue - 1, root.val) && helper(root.right, root.val, (long)int.MaxValue + 1);
        }
    }
}