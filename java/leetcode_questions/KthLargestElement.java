package leetcode_questions;
import java.util.PriorityQueue;

/**
 * KthLargestElement
 */
public class KthLargestElement
{
    // public static final F<Integer, Integer> timesTwo = i -> i * 2;

    public static int findKthLargest(Integer[] nums, int k)
    {
        // List<Integer> lst = Arrays.asList(Arrays.stream(nums).boxed().toArray(Integer[]::new));

        var minheap = new PriorityQueue<Integer>(k + 1);

        for (var num : nums)
        {
            minheap.add(num);

            if (minheap.size() > k)
            {
                minheap.remove();
            }
        }

        return minheap.peek();
    }

}