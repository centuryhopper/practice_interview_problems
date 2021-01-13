public class RangeSumQuery
{
    int[] arr;

    public RangeSumQuery(int[] nums)
    {
        arr = nums;
    }

    public int SumRange(int i, int j)
    {
	// arr[i..j] would get the subarray of elements from i to j, but not including
	// the item at index j, so we offset the j by the adding one to include it in our addition operation
        return arr[i..(j+1)].Sum();
    }
}