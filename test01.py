# pylint: disable=invalid-name

from tqdm import tqdm


def number_of_ways(startPos: int, endPos: int, k: int) -> int:

    """
    Solve Leetcode Problem:
    https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/
    """

    # Each element in `paths` is a list representing a path taken
    paths = [[startPos]]

    for i in tqdm(range(k)):
        new_paths = []  # Store new paths in a separate list
        for path in paths:
            last_position = path[-1]

            # Early exit if we can't possibly reach endPos in remaining steps
            if abs(endPos - last_position) > (k - i):
                # skip generating new paths
                continue

            # Path that goes left
            new_path_left = path + [last_position - 1]
            # Path that goes right
            new_path_right = path + [last_position + 1]

            # Add both to new_paths
            new_paths.append(new_path_left)
            new_paths.append(new_path_right)

        # Update `paths` at the end of the iteration
        paths = new_paths

    # Count how many paths end at `endPos`
    num_ways = 0
    for path in paths:
        if path[-1] == endPos:
            num_ways += 1

    return num_ways


def test_number_of_ways():
    """
    Example:
    startPos = 1, endPos = 2, k = 3
    Expected output: 3
    """
    ways = number_of_ways(1, 2, 3)
    print(f"Number of ways (1 -> 2 in exactly 3 steps): {ways}")


if __name__ == "__main__":
    test_number_of_ways()