def find_height(root):
    if root is None:
        return -1  # or 0 depending on convention
    left_height = find_height(root.left)
    right_height = find_height(root.right)
    return max(left_height, right_height) + 1
