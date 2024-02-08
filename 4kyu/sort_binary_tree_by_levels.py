import codewars_test as test


class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(root):
    if root is None:
        return []

    queue = [root]
    vals = []
    vals.append(root.value)

    while len(queue) > 0:
        cur_node = queue.pop(0)

        if cur_node.left is not None:
            vals.append(cur_node.left.value)
            queue.append(cur_node.left)

        if cur_node.right is not None:
            vals.append(cur_node.right.value)
            queue.append(cur_node.right)

    return vals

test.assert_equals(tree_by_levels(None), [])
test.assert_equals(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(
    Node(None, None, 5), Node(None, None, 6), 3), 1)), [1, 2, 3, 4, 5, 6])
