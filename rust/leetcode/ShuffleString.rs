impl Solution
{
    pub fn restore_string(s: String, indices: Vec<i32>) -> String
    {
        // Convert string to char array then populate accordingly
        let mut lst: Vec<char> = s.chars().collect();
        let n = s.len();

        for (i, ind) in indices.iter().enumerate()
        {
            lst[*ind as usize] = s.chars().nth(i).unwrap();
        }

        lst.into_iter().collect()
    }
}

// 03/05/2023
