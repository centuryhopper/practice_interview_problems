using System.Collections.Generic;
using System;

public class Atoi
{
    public int MyAtoi(string s)
    {
        if (string.IsNullOrEmpty(s))
        {
            return 0;
        }

        int i = 0;
        int ret = 0;
        int n = s.Length;
        bool isNeg = false;

        // or we could use Char.IsDigit() but I ain't relying on library functions
        var set = new HashSet<char>() { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };

        // skip whitespaces
        while (i < n && s[i] == ' ')
        {
            i += 1;
        }

        if (i < n && s[i] == '-')
        {
            isNeg = true;
            i += 1;
        }
        else if (i < n && s[i] == '+')
        {
            isNeg = false;
            i += 1;
        }


        while (i < n)
        {
            if (!set.Contains(s[i]) && ret > 0)
            {
                // return what we already have
                return isNeg ? -ret : ret;
            }

            // if we encounter a non-numeric character
            // we leave regardless of what characters come next
            if (!set.Contains(s[i]))
            {
                return 0;
            }

            int num = s[i] - '0';
            // check for integer overflow to see whether the current 'num' is safe to append or not
            if (ret > int.MaxValue / 10 || ret == int.MaxValue / 10 && num >= 8)
            {
                return isNeg ? int.MinValue : int.MaxValue;
            }

            ret *= 10;
            ret += num;
            i += 1;
        }

        return isNeg ? -ret : ret;
    }
}




#region bad solution
// public int MyAtoi(string s)
//     {
//         // todo check for int max and int mins

//         s = s.Trim();

//         // print(s.Length);
//         long res = 0;
//         bool isNeg = false;

//         int n = s.Length;

//         for (int i = 0; i < n; ++i)
//         {
//             long c = s[i] - '0';
//             if (c >= 0 && c <= 9)
//             {
//                 res *= 10;
//                 res += c;

//                 if (i < n-1 && (s[i+1] != ' ' && !Char.IsDigit(s[i+1])))
//                 {
//                     if (s[i+1] == '.')
//                     {
//                         break;
//                     }
//                     return 0;
//                 }
//             }
//             else if (s[i] == '-')
//             {
//                 isNeg = true;
//                 if (i < n-1 && s[i] == '-' && !Char.IsDigit(s[i+1]))
//                 {
//                     print(s[i+1]);
//                     break;
//                 }
//             }
//             else if (s[i] == '+')
//             {
//                 if (i < n-1 && s[i] == '+' && !Char.IsDigit(s[i+1]))
//                 {
//                     print(s[i+1]);
//                     break;
//                 }
//             }
//             else
//             {
//                 break;
//             }
//         }

//         if (isNeg)
//         {
//             res *= -1;
//         }

//         if (res > int.MaxValue)
//         {
//             return int.MaxValue;
//         }

//         if (res < int.MinValue)
//         {
//             return int.MinValue;
//         }



//         return (int)res;
//     }
#endregion