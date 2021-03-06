# V0 

# V1 
# https://blog.csdn.net/fuxuemingzhu/article/details/82827177
# https://www.youtube.com/watch?v=VlZiMD7Iby4
# IDEA : BFS 
class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        for dislike in dislikes:
            graph[dislike[0] - 1].append(dislike[1] - 1)
            graph[dislike[1] - 1].append(dislike[0] - 1)
        color = [0] * N
        for i in range(N):
            if color[i] != 0: continue
            bfs = collections.deque()
            bfs.append(i)
            color[i] = 1
            while bfs:
                cur = bfs.popleft()
                for e in graph[cur]:
                    if color[e] != 0:
                        if color[cur] == color[e]:
                            return False
                    else:
                        color[e] = -color[cur]
                        bfs.append(e)
        return True
 
# V1'
# IDEA : DFS 
       
# V2 
# Time:  O(|V| + |E|)
# Space: O(|V| + |E|)
import collections
class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        adj = [[] for _ in range(N)]
        for u, v in dislikes:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)

        color = [0]*N
        color[0] = 1
        q = collections.deque([0])
        while q:
            cur = q.popleft()
            for nei in adj[cur]:
                if color[nei] == color[cur]:
                    return False
                elif color[nei] == -color[cur]:
                    continue
                color[nei] = -color[cur]
                q.append(nei)
        return True
