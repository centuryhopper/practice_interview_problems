impl Solution
{
    pub fn reverse_string(s: &mut Vec<char>)
    {
        let n = s.len();
        if n < 2
        {
            return
        }
        let (mut i,mut j) = (0, n-1);

        while (i < j)
        {
            s.swap(i,j);
            i+=1;
            j-=1;
        }
    }
}

// 03/04/2023
//
