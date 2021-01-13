
using System;
using System.Text;

public class CheckStringArrayEquivalence
{
    public bool ArrayStringsAreEqual(string[] word1, string[] word2)
    {
        var sb1 = new StringBuilder();
        var sb2 = new StringBuilder();

        int len1 = word1.Length, len2 = word2.Length;
        int n = Math.Max(len1, len2);

        for (int i = 0; i < n; ++i)
        {
            if (i < len1)
                sb1.Append(word1[i]);
            if (i < len2)
                sb2.Append(word2[i]);
        }

        return sb1.ToString().Equals(sb2.ToString());
    }
}
