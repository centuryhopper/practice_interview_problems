impl Solution
{
    pub fn reverse_words(s: String) -> String
    {
        // can also do: let mut vec: Vec<&str> = s.split(" ").collect();
        let mut vec: Vec<_> = s.split(" ").filter(|&x| !x.is_empty()).collect();
        vec.reverse();
        // println!("{:?}", vec);

        vec.join(" ")
    }
}
