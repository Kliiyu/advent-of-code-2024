def count_xmas(grid, word="XMAS"):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    count = 0

    def check_direction(start_row, start_col, delta_row, delta_col):
        for i in range(word_len):
            r = start_row + i * delta_row
            c = start_col + i * delta_col
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != word[i]:
                return False
        return True

    for row in range(rows):
        for col in range(cols):
            directions = [
                (0, 1),   # Right
                (0, -1),  # Left
                (1, 0),   # Down
                (-1, 0),  # Up
                (1, 1),   # Down-Right
                (-1, -1), # Up-Left
                (1, -1),  # Down-Left
                (-1, 1)   # Up-Right
            ]
            for delta_row, delta_col in directions:
                if check_direction(row, col, delta_row, delta_col):
                    count += 1
    return count

def main():
    result = 0
    try:
        with open('day_4/input.txt', 'r') as f:
            lines = f.readlines()
            grid = [line.strip() for line in lines]
            grid = [list(row) for row in grid]
            result = count_xmas(grid)
                
    except FileNotFoundError:
        print("The file 'input.txt' was not found.")
    return result

if __name__ == '__main__':
    result = main()
    print(f"XMAS appears: {result} times.")