# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f'<{self.val}, {self.left}, {self.right}>'

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def search_by_key(self, key):
        # Base Cases: root is null or key is present at root
        if self is None or self.val == key:
            return self

        lft = None
        rght = None
        # Key is greater than root's key
        if self.left is not None:
            lft = self.left.search_by_key(key)
        if lft is not None:
            return lft
        if self.right is not None:
            rght = self.right.search_by_key(key)
        if rght is not None:
            return rght
        return None

    def search_by_node(self, node):
        # Base Cases: root is null or key is present at root
        if self is node:
            return self

        lft = None
        rght = None
        # Key is greater than root's key
        if self.left is not None:
            lft = self.left.search_by_node(node)
        if lft is not None:
            return lft
        if self.right is not None:
            rght = self.right.search_by_node(node)
        if rght is not None:
            return rght

        return None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        path = path_to_node(original, target)
        # print("path:", path)
        node = cloned
        for el in path:
            # print("path element:", el)
            # print("target.val:", target.val)
            # print("node:", node)
            # print("node.left:", node.left)
            # print("node.right:", node.right)
            # print("cond node.val == el:", node.val == el)
            if node is not None and node.val == target.val:
                # print("entering if")
                return node
            elif node is not None and node.val == el:
                # print("entering elif 1")
                # node = node
                pass
            elif node.left is not None and node.left.val == el:
                # print("entering elif 2")
                node = node.left
            elif node.right is not None and node.right.val == el:
                # print("entering elif 3")
                node = node.right
        return node


def path_to_node(root, node):
    # Base Cases: root is null or key is present at root
    if root is node:
        return [root.val]

    lft = []
    rght = []
    # Key is greater than root's key
    if root.left is not None:
        res_lft = path_to_node(root.left, node)
        if len(res_lft) > 0:
            lft += [root.val]
            lft += res_lft
    if len(lft) > 0:
        return lft
    if root.right is not None:
        res_rght = path_to_node(root.right, node)
        if len(res_rght) > 0:
            rght += [root.val]
            rght += res_rght
    if len(rght) > 0:
        return rght

    return []


def build_binary_tree(values, index=0):
    if len(values) == 0:
        raise Exception('Node list is empty')

    if index > len(values) - 1:
        raise Exception('Index out of range')

    root = TreeNode(values[index])
    if 2 * index + 1 < len(values):
        root.left = build_binary_tree(values, 2 * index + 1)
    if 2 * index + 2 < len(values):
        root.right = build_binary_tree(values, 2 * index + 2)

    return root





sl = Solution()
tree1 = [7, 4, 3, None, None, 6, 19]
target1 = 3

tree2 = [7]
target2 = 7

tree3 = [8, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1]
target3 = 4

tree4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target4 = 5

tree5 = [1, 2, None, 3]
target5 = 2

tr1 = build_binary_tree(tree1)
cl1 = build_binary_tree(tree1)
print("Tree 1")
tr1.display()
trgt1 = tr1.search_by_key(target1)
print("Target:", target1, "Path:", path_to_node(tr1, trgt1))
print("Node found:", sl.getTargetCopy(tr1, cl1, trgt1))
print()

tr2 = build_binary_tree(tree2)
cl2 = build_binary_tree(tree2)
print("Tree 2")
tr2.display()
trgt2 = tr2.search_by_key(target2)
print("Target:", target2, "Path:", path_to_node(tr2, trgt2))
print("Node found:", sl.getTargetCopy(tr2, cl2, trgt2))
print()

tr3 = build_binary_tree(tree3)
cl3 = build_binary_tree(tree3)
print("Tree 3")
tr3.display()
trgt3 = tr3.search_by_key(target3)
print("Target:", target3, "Path:", path_to_node(tr3, trgt3))
print("Node found:", sl.getTargetCopy(tr3, cl3, trgt3))
print()

tr4 = build_binary_tree(tree4)
cl4 = build_binary_tree(tree4)
print("Tree 4")
tr4.display()
trgt4 = tr4.search_by_key(target4)
print("Target:", target4, "Path:", path_to_node(tr4, trgt4))
print("Node found:", sl.getTargetCopy(tr4, cl4, trgt4))
print()

tr5 = build_binary_tree(tree5)
cl5 = build_binary_tree(tree5)
print("Tree 5")
tr5.display()
trgt5 = tr5.search_by_key(target5)
print("Target:", target5, "Path:", path_to_node(tr5, trgt5))
print("Node found:", sl.getTargetCopy(tr5, cl5, trgt5))
print()
