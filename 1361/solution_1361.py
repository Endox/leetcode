from collections import deque
from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        merged = {*leftChild, *rightChild}
        root_candidates = [node for node in range(n) if node not in merged]
        if len(root_candidates) != 1:
            return False

        root = root_candidates[0]

        passed = [False] * n
        parent_known = deque([root])

        while parent_known:
            current = parent_known.popleft()

            children = [child for child in [leftChild[current], rightChild[current]] if child != -1]

            if any([(child == current or child in parent_known or passed[child]) for child in children]):
                return False

            parent_known.extend(children)
            passed[current] = True

        return all(passed)



