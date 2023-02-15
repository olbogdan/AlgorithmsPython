# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
#
# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
#
#
#
# Example 1:
#
#
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
# Example 2:
#
# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1
# Example 3:
#
# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1
#
#
# Constraints:
#
# 1 <= k <= n <= 100
# 1 <= times.length <= 6000
# times[i].length == 3
# 1 <= ui, vi <= n
# ui != vi
# 0 <= wi <= 100
# All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
from collections import defaultdict
from heapq import heappush, heappop
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for src, dist, time in times:
            adj[src].append((time, dist))

        q = [(0, k)]
        result = 0
        visited = set()
        while q:

            time, node = heappop(q)

            # optional optimization
            if len(visited) == n:
                return result
            if node in visited:
                continue
            visited.add(node)
            result = time

            for childTime, child in adj[node]:
                if child not in visited:
                    heappush(q, (childTime + time, child))
        if len(visited) != n:
            return -1
        return result


sol = Solution()
assert sol.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2
assert sol.networkDelayTime([[1,2,1]], 2, 1) == 1
assert sol.networkDelayTime([[1,2,1]], 2, 2) == -1
