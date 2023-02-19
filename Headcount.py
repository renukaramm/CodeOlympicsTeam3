
def headcount(layout):
    rows, columns = len(layout), len(layout[0])
    team_counts = []
    for i in range(rows):
        for j in range(columns):
            if layout[i][j] & 1:
                team_size = 0
                stack = [(i, j)]
                while stack:
                    row, column = stack.pop()
                    if layout[row][column] & 1:
                        team_size += 1
                        layout[row][column] ^= 1
                        for r, c in (
                            (row - 1, column),
                            (row + 1, column),
                            (row, column - 1),
                            (row, column + 1),
                        ):
                            if 0 <= r < rows and 0 <= c < columns and layout[r][c] & 1:
                                stack.append((r, c))
                team_counts.append(team_size)
    total_headcount = sum(team_counts)
    return f"{len(team_counts)} teams of {sorted(team_counts, reverse=True)} totaling {total_headcount}"

print(
    headcount(
        [
            [1, 1, 0, 0, 0, 0, 1, 1],
            [1, 1, 0, 1, 1, 0, 1, 1],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [1, 1, 0, 1, 1, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 1, 1],
        ]
    )
)




