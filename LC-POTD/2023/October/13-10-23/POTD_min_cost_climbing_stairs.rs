// POTD Otober 13, 2023
// Minimum Cost Climbing Stairs
// Link - https://leetcode.com/problems/min-cost-climbing-stairs/?envType=daily-question&envId=2023-10-13

// Implementation of the Solution struct
impl Solution {
    // Function to find the minimum cost of climbing stairs
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        // Get the length of the cost vector
        let n = cost.len();

        // Initialize variables to keep track of previous two costs
        let mut prev = 0;
        let mut pprev = 0;

        // Iterate through the cost vector starting from the 2nd element
        for i in 2..=n {
            // Calculate the current cost by choosing the minimum of two options
            let curr = std::cmp::min(prev + cost[i - 1], pprev + cost[i - 2]);

            // Update previous two costs for the next iteration
            pprev = prev;
            prev = curr;
        }

        // Return the final result, which is the minimum cost to reach the top
        prev
    }
}
