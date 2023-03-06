impl Solution {
    pub fn rotate_string(s: String, goal: String) -> bool
    {
        let m = s.len(); 
        let n = goal.len();
        if m != n { return false; }

        let mut v : Vec<char> = s.chars().collect();

        // keep shifting until we make a full circle
        for _ in 1..=m
        {
            // println!("hi");
            let first : char = v.remove(0);
            v.push(first);
            if v.iter().collect::<String>().as_str() == goal
            {
                return true;
            }
        }

        false
    }
}

// 03/04/2023
//
