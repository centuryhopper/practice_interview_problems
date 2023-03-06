impl Solution {
    pub fn di_string_match(s: String) -> Vec<i32> {
        let n = s.len();
        let (mut lo, mut hi) = (0, n);
        let mut perm: Vec<i32> = vec![];
        for c in s.chars()
        {
            // println!("{}",c);
            match c
            {
                'I' => {
                    perm.push(lo as i32);
                    lo+=1;
                }
                'D' => {
                    perm.push(hi as i32);
                    hi-=1;
                }
                _ => {
                    println!("we really shouldn't reach here if we only get D's and I's");
                }
            }
        }
        
        // println!("{} {}", lo, hi);
        // get the last number in our [0,n] range into the array (edge case)
        perm.push(lo);

        perm
        
    }
}

// 03/05/2023
//
