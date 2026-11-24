class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board, words):
        root = TrieNode()

        # Build Trie
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, parent):
            ch = board[r][c]

            if ch not in parent.children:
                return

            node = parent.children[ch]

            if node.word is not None:
                result.append(node.word)
                node.word = None

            board[r][c] = '#'

            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] != '#':
                        dfs(nr, nc, node)

            board[r][c] = ch

            # Remove exhausted Trie branches
            if not node.children and node.word is None:
                del parent.children[ch]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result