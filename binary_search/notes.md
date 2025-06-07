# Binary Tree Algorithms and Concepts - Summary

This document summarizes everything we've learned about binary trees today, with a focus on understanding, traversals, transformations, and problem-solving using recursion and DFS. It's tailored for Meta interview prep.

---

## ✅ 1. Validating a Binary Search Tree (BST)
**Problem:** Determine if a binary tree is a valid BST.

### Key Rule:
- Left subtree < node < Right subtree (recursively true for all nodes)

### Algorithm:
- Use DFS with `low` and `high` bounds.
- Start with `(-inf, inf)` bounds at the root.
- On left call: update `high = node.val`
- On right call: update `low = node.val`

```python
import math

def isValidBST(root):
    def dfs(node, low=-math.inf, high=math.inf):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

    return dfs(root)
```

---

## ✅ 2. Inserting into a Binary Search Tree
**Problem:** Insert a value into the BST.

### Algorithm:
- If root is `None`, return a new node.
- If value < root.val: go left
- Else: go right
- Recurse until insertion point found.

```python
def insertBST(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insertBST(root.left, val)
    else:
        root.right = insertBST(root.right, val)
    return root
```

---

## ✅ 3. Flatten Binary Tree to Linked List
**Problem:** Convert a binary tree to a linked list in-place using pre-order traversal.

### Strategy:
- Store nodes in a pre-order list
- Iterate through list and update `left = None`, `right = next node`

```python
def flatten(root):
    if not root:
        return

    nodes = []

    def preorder(node):
        if not node:
            return
        nodes.append(node)
        preorder(node.left)
        preorder(node.right)

    preorder(root)

    for i in range(1, len(nodes)):
        prev = nodes[i - 1]
        curr = nodes[i]
        prev.left = None
        prev.right = curr
```

---

## ✅ 4. Depth-First Search (DFS) Traversal
### Purpose:
- Visit all nodes in a binary tree in a particular order.

### Preorder Traversal:
- Root -> Left -> Right

### Code:
```python
def dfs_traversal(root):
    result = []

    def dfs(node):
        if not node:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return result
```

---

## ✅ 5. Maximum Path Sum in a Binary Tree
**Problem:** Find the path in the tree with the maximum sum (not necessarily passing through root).

### Strategy:
- Use DFS
- Track the max sum seen globally (nonlocal variable)
- At each node: `max_gain = node.val + max(left_gain, right_gain, 0)`

```python
def maxPathSum(root):
    max_sum = float('-inf')

    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0

        left = max(dfs(node.left), 0)
        right = max(dfs(node.right), 0)

        max_sum = max(max_sum, node.val + left + right)

        return node.val + max(left, right)

    dfs(root)
    return max_sum
```

---

## Key Concepts & Tips:
- **DFS:** Great for recursive tree problems (traversal, max path, validation).
- **Bounds Logic in BST:** Critical for validating trees.
- **In-place Transformations:** Modify tree structure using pointer rewiring.
- **Nonlocal Keyword:** Used when modifying variables in an outer (non-global) function.
- **float('-inf') vs 0:** Use `-inf` for safety in max calculations involving negative numbers.

---

Let me know if you want to turn this into a downloadable PDF or add diagrams or example walkthroughs for each section!
