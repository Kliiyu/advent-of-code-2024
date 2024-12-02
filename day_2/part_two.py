def is_safe(levels):
    return all(1 <= abs(levels[i] - levels[i+1]) <= 3 for i in range(len(levels) - 1)) and \
           (all(levels[i] < levels[i+1] for i in range(len(levels) - 1)) or all(levels[i] > levels[i+1] for i in range(len(levels) - 1)))

def main():
    total_safe = 0
    try:
        with open('day_2/input.txt', 'r') as f:
            lines = f.readlines()
            
            for line in lines:
                levels = list(map(int, line.split(' ')))

                if is_safe(levels):
                    total_safe += 1
                else:
                    for i in range(len(levels)):
                        new_levels = levels[:i] + levels[i+1:]
                        if is_safe(new_levels):
                            total_safe += 1
                            break
                
    except FileNotFoundError:
        print("The file 'input.txt' was not found.")
    return total_safe

if __name__ == '__main__':
    total_safe = main()
    print(f"A total of {total_safe} are safe.")