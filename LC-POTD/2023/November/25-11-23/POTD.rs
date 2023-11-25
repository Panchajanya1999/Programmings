impl Solution {
    pub fn get_sum_absolute_differences(nums: Vec<i32>) -> Vec<i32> {

        let n = nums.len();
        // Calculate the prefix and suffix sums
        let mut prefix_sums = vec![0; n];
        let mut suffix_sums = vec![0; n];
        
        prefix_sums[0] = nums[0];
        for i in 1..n {
            prefix_sums[i] = prefix_sums[i - 1] + nums[i];
        }
        
        suffix_sums[n - 1] = nums[n - 1];
        for i in (0..n - 1).rev() {
            suffix_sums[i] = suffix_sums[i + 1] + nums[i];
        }
        
        let mut res = vec![0; n];
        
        // Calculate the absolute differences using prefix and suffix sums
        for i in 0..n {
            let left_sum = i as i32 * nums[i] - prefix_sums[i];
            let right_sum = suffix_sums[i] - (n - i - 1) as i32 * nums[i];
            
            res[i] = left_sum + right_sum;
        }
        
        res
    }
}
