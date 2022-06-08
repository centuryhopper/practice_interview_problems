import leetcode_questions.KthLargestElement;
import leetcode_questions.LetterCasePermutation;
import interfaces.*;

public class Main
{
    private static class myPair1 implements CustomPair1
    {
        public Object [] array;
        public Object k;

        public myPair1(Integer[] a, int k)
        {
            array = a; this.k = k;
        }
    }

    static void p(Object msg)  {System.out.println(msg);}

    public static void main(String[] args)
    {

        // Integer[] test = {3,2,1,5,6,4}, test2 = {3,2,3,1,2,4,5,5,6};

        // myPair1 pair = new myPair1((Integer[]) test, (int) 2);

        // assert KthLargestElement.findKthLargest(test2, 4) == 4;
        // assert KthLargestElement.findKthLargest((Integer[]) pair.array, (int) pair.k) == 5;

        // System.out.println();

        p("");

        long start = System.currentTimeMillis();

        LetterCasePermutation l = new LetterCasePermutation();

        l.letterCasePermutation("a1b2").forEach(i -> p(i));
        l.letterCasePermutation("3z4").forEach(i -> p(i));
        l.letterCasePermutation("12345").forEach(i -> p(i));
        l.letterCasePermutation("0").forEach(i -> p(i));

        p("time: " + (System.currentTimeMillis() - start) + " ms");
    }

}
