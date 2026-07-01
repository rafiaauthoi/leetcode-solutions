class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = {i: set() for i in range(9)}
        cols = {i: set() for i in range(9)}
        boxes = {}

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                box_id = (r // 3, c // 3)
                if box_id not in boxes:
                    boxes[box_id] = set()

                if val in rows[r] or val in cols[c] or val in boxes[box_id]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_id].add(val)

        return True