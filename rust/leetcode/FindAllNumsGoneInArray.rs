use std::vec;


impl Solution
{
    /*
    n = len(nums)
        ans = []
        for i, num in enumerate(nums):
                nums[abs(num)-1] = -abs(nums[abs(num)-1])
        # print(nums)
        for i,num in enumerate(nums):
            if num > 0:
                ans.append(i+1)

        return ans
    */
    pub fn find_disappeared_numbers(nums: Vec<i32>) -> Vec<i32>
    {
        let n = nums.len();
        let mut tmp = nums.to_vec();
        let mut ans:Vec<i32> = Vec::new();
        // mark necesary numbers as negative
        for (i, num) in nums.iter().enumerate()
        {
            tmp[(num.abs()-1) as usize] = -nums[(num.abs()-1) as usize].abs();
        }
        // println!("{:?}",tmp);
        // all remaining positive numbers' index + 1 will be the missing numbers
        for (i, num) in tmp.iter().enumerate()
        {
            if num.is_positive()
            {
                ans.push((i+1) as i32);
            }
        }

        return ans as Vec<i32>;

    }
}