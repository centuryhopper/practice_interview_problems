

using System.Collections.Generic;
using data_structures;

namespace practice_problems
{
    public class PseudoPalindromicPathsInBT
    {
        private bool CanPotentiallyFormPalindrome(Dictionary<int, int> d, TreeNode leaf)
        {
            int odds = 0;

            //      remembering to record leaf node values
            if (!d.TryAdd(leaf.val, 1))
            {
                d[leaf.val]++;
            }

            // checking for multiple odds
            foreach (var i in d)
            {
                if (odds > 1) return false;

                if (i.Value % 2 == 1)
                {
                    odds++;
                }
            }

            return true;
        }

        private int helper(TreeNode root, Dictionary<int, int> d)
        {
            if (root == null) return 0;

            //         check only at leaf nodes otherwise dfs left and right
            if (root.left == null && root.right == null)
            {

                int odds = 0;
                // remembering to record leaf node values
                if (!d.TryAdd(root.val, 1))
                {
                    d[root.val]++;
                }

                foreach (var v in d.Values)
                {
                    if (v % 2 == 1)
                    {
                        odds++;
                    }
                }

                // undo state change
                d[root.val]--;
                if (odds > 1) return 0;

                return 1;
            }
            else
            {
                if (!d.TryAdd(root.val, 1))
                {
                    d[root.val]++;
                }

                // dfs left and right
                int res = helper(root.left, d) + helper(root.right, d);

                // undo state change
                d[root.val]--;

                return res;
            }
        }


        public int PseudoPalindromicPaths(TreeNode root)
        {
            if (root == null) return 0;

            var d = new Dictionary<int, int>();

            return helper(root, d);
        }
    }
}