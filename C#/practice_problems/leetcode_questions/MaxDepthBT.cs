using data_structures;

namespace practice_problems
{
    public class Solution
    {
        public int MaxDepth(TreeNode root)
        {
            if (root == null) return 0;
            if (root.left == null && root.right == null)
            {
                return 1;
            }

            int cnt = 1 + System.Math.Max(MaxDepth(root.left), MaxDepth(root.right));

            return cnt;
        }
    }
}