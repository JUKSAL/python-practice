import tqdm
from tqdm import tqdm


from tqdm import tqdm

def numberOfWays(startPos: int, endPos: int, k: int) -> int:
    """
    Solving Leetcode Problem:
    https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/
    
    Given two positive integers startPos and endPos, determine the number of ways
    to reach endPos from startPos using exactly k steps.

    Constraints:
    - Each step can move either +1 (right) or -1 (left).
    """
    from collections import defaultdict

    # Memoization for efficiency
    memo = {}

    def dfs(pos, steps):
        if steps == 0:
            return 1 if pos == endPos else 0
        if (pos, steps) in memo:
            return memo[(pos, steps)]
        
        # Move left or right
        memo[(pos, steps)] = dfs(pos - 1, steps - 1) + dfs(pos + 1, steps - 1)
        return memo[(pos, steps)]

    return dfs(startPos, k)


def test_number_of_ways():
    """
    Test case:
    startPos = 1, endPos = 2, k = 3
    Expected output: 3
    """
    result = numberOfWays(1, 2, 3)
    print(f"Result: {result}")

if __name__ == "__main__":
    test_number_of_ways()
