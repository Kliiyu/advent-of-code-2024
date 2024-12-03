import re

def main():
    result = 0
    try:
        with open('day_3/input.txt', 'r') as f:
            lines = f.readlines()
            mul_list = []
            for line in lines:
                matches = re.findall(r'mul\((\d+),\s*(\d+)\)', line)
                for match in matches:
                    x, y = map(int, match)
                    mul_list.append((x, y))
            result = sum(x * y for x, y in mul_list)
                
    except FileNotFoundError:
        print("The file 'input.txt' was not found.")
    return result

if __name__ == '__main__':  
    result = main()
    print(f"The total of the multiplications is: {result}")