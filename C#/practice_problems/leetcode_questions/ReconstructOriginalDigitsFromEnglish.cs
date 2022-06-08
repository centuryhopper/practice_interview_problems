using System;
using System.Text;

public class ReconstructOriginalDigitsFromEnglish
{
    
    static void p(object m) => Console.WriteLine(m);

    public string OriginalDigits(string s)
    {
        int[] cnts = new int[26];
        foreach (char letter in s)
        {
            ++cnts[letter - 'a'];
            // p(letter);
        }
        // p(string.Join(" ", cnts));

        int[] num = new int[10];
        // unique cases
        num[0] = cnts['z' - 'a'];
        num[2] = cnts['w' - 'a'];
        num[4] = cnts['u' - 'a'];
        num[6] = cnts['x' - 'a'];
        num[8] = cnts['g' - 'a'];
        // derived cases
        num[1] = cnts['o' - 'a'] - num[0] - num[2] - num[4];
        num[3] = cnts['h' - 'a'] - num[8];
        num[5] = cnts['f' - 'a'] - num[4];
        num[7] = cnts['s' - 'a'] - num[6];
        num[9] = cnts['i' - 'a'] - num[6] - num[8] - num[5];

        var sb = new StringBuilder();
        for (int i = 0; i < num.Length; ++i)
        {
            // exhaust the cnt
            while (num[i]-- > 0)
            {
                sb.Append(i);
            }
        }

        return sb.ToString();

    }


    #region optimized solution
    // public string OriginalDigits(string s)
    // {
    //     int[] letterCnt = new int[26];
    //     for (int i = 0; i < s.Length; i++)
    //     {
    //         letterCnt[s[i] - 'a'] = letterCnt[s[i] - 'a'] + 1;
    //     }
    //     int[] digit = new int[10];
    //     while (letterCnt['z' - 'a'] > 0)
    //     {
    //         letterCnt['z' - 'a']--;
    //         letterCnt['e' - 'a']--;
    //         letterCnt['r' - 'a']--;
    //         letterCnt['o' - 'a']--;
    //         digit[0]++;
    //     }
    //     while (letterCnt['w' - 'a'] > 0)
    //     {
    //         letterCnt['t' - 'a']--;
    //         letterCnt['w' - 'a']--;
    //         letterCnt['o' - 'a']--;
    //         digit[2]++;
    //     }
    //     while (letterCnt['u' - 'a'] > 0)
    //     {
    //         letterCnt['f' - 'a']--;
    //         letterCnt['o' - 'a']--;
    //         letterCnt['u' - 'a']--;
    //         letterCnt['r' - 'a']--;
    //         digit[4]++;
    //     }
    //     while (letterCnt['x' - 'a'] > 0)
    //     {
    //         letterCnt['s' - 'a']--;
    //         letterCnt['i' - 'a']--;
    //         letterCnt['x' - 'a']--;

    //         digit[6]++;
    //     }
    //     while (letterCnt['g' - 'a'] > 0)
    //     {
    //         letterCnt['e' - 'a']--;
    //         letterCnt['i' - 'a']--;
    //         letterCnt['g' - 'a']--;
    //         letterCnt['h' - 'a']--;
    //         letterCnt['t' - 'a']--;
    //         digit[8]++;
    //     }
    //     while (letterCnt['o' - 'a'] > 0)
    //     {
    //         letterCnt['o' - 'a']--;
    //         letterCnt['n' - 'a']--;
    //         letterCnt['e' - 'a']--;
    //         digit[1]++;
    //     }
    //     while (letterCnt['t' - 'a'] > 0)
    //     {
    //         letterCnt['t' - 'a']--;
    //         letterCnt['h' - 'a']--;
    //         letterCnt['r' - 'a']--;
    //         letterCnt['e' - 'a']--;
    //         letterCnt['e' - 'a']--;
    //         digit[3]++;
    //     }
    //     while (letterCnt['f' - 'a'] > 0)
    //     {
    //         letterCnt['f' - 'a']--;
    //         letterCnt['i' - 'a']--;
    //         letterCnt['v' - 'a']--;
    //         letterCnt['e' - 'a']--;
    //         digit[5]++;
    //     }
    //     while (letterCnt['v' - 'a'] > 0)
    //     {
    //         letterCnt['s' - 'a']--;
    //         letterCnt['e' - 'a']--;
    //         letterCnt['v' - 'a']--;
    //         letterCnt['e' - 'a']--;
    //         letterCnt['n' - 'a']--;
    //         digit[7]++;
    //     }
    //     while (letterCnt['i' - 'a'] > 0)
    //     {
    //         letterCnt['n' - 'a']--;
    //         letterCnt['i' - 'a']--;
    //         letterCnt['n' - 'a']--;
    //         letterCnt['e' - 'a']--;
    //         digit[9]++;
    //     }
    //     StringBuilder sb = new StringBuilder();
    //     for (int i = 0; i < 10; i++)
    //     {

    //         for (int j = 0; j < digit[i]; j++)
    //         {
    //             sb.Append((char)(i + '0'));
    //         }
    //     }
    //     return sb.ToString();
    // }
    #endregion
}