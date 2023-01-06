

'''
You are given an m x n matrix grid consisting of positive integers.

Perform the following operation until grid becomes empty:

Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
Add the maximum of deleted elements to the answer.
Note that the number of columns decreases by one after each operation.

Return the answer after performing the operations described above.

'''


def deleteGreatestValue(grid) -> int:
    result = 0

    while len(grid[0]) > 0:
        values = []
        for row in grid:
            max_in_row = max(row)
            values.append(max_in_row)
            row.remove(max_in_row)

        result += max(values)

    return result


grid = [[1, 2, 4], [3, 3, 1]]

print('res => ', deleteGreatestValue(grid))

grid = [[10]]

print('res => ', deleteGreatestValue(grid))
