public class ArrayOfDoubledPairs {
    void print(Object msg)
    {
        System.out.println(msg);
    }
    public boolean canReorderDoubled(int[] arr) {
        // # use frequency hashmap tp check for dups of nonzero numbers. If any exist, then return false
        // # otherwise check to see if the first half of the array, after it's sorted, has doubles
        var d = new HashMap<Integer,Integer>();
        for (int num : arr)
        {
            d.put(num, d.getOrDefault(num,0)+1);
        }
        // # handle zero cases
        // # there must be an even number of zeros
        if (d.containsKey(0) && d.get(0) % 2 == 1)
            return false;
        int n = arr.length;
        int cnt = 0;
        Arrays.sort(arr);
        for (int num: arr)
        {
            // # if the current value's double exists and the current value hasn't been paired yet
            if (d.getOrDefault(2*num,0) != 0 && d.getOrDefault(num,0) != 0)
            {
                // # lst.append((num,2*num))
                cnt+=1;
                // # decrement both
                d.put(2*num, Math.max(0,d.get(2*num)-1));
                d.put(num, Math.max(0,d.get(num)-1));
            }
        }
            
        return cnt == n/2;
        
    }
}