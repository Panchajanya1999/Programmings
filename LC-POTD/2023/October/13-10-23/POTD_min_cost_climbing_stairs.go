// POTD Otober 13, 2023
// Minimum Cost Climbing Stairs
// Link - https://leetcode.com/problems/min-cost-climbing-stairs/?envType=daily-question&envId=2023-10-13


func minCostClimbingStairs(cost []int) int {
    // Get the length of the cost slice
	n := len(cost)

	// Initialize variables to keep track of previous two costs
	var prev, pprev int

	// Iterate through the cost slice starting from the 2nd element
	for i := 2; i <= n; i++ {
		// Calculate the current cost by choosing the minimum of two options
		curr := min(prev+cost[i-1], pprev+cost[i-2])

		// Update previous two costs for the next iteration
		pprev, prev = prev, curr
	}

	// Return the final result, which is the minimum cost to reach the top
	return prev
}

// Helper function to find the minimum of two integers
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}