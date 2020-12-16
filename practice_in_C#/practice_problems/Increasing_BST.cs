using data_structures;

namespace practice_problems
{
    public class Increasing_BST
    {
        TreeNode current;

        private void helper(TreeNode root)
        {
            if (root == null) return;

            helper(root.left);

            // sever the left child
            root.left = null;
            current.right = root;
            current = current.right;

            helper(root.right);
        }

        public TreeNode IncreasingBST(TreeNode root)
        {
            TreeNode head = new TreeNode();
            current = head;

            helper(root);

            return head.right;
        }
    }
}