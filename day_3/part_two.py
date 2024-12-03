import re

def main():
    try:
        with open('day_3/input.txt', 'r') as f:
            data = f.read()

        pattern = r"mul\(\d+,\d+\)|do\(+\)|don\'t\(+\)"
        instructions = re.findall(pattern, data)

        result = 0
        flag = True
        for instruction in instructions:    
            if instruction == "don't()":
                flag = False
            elif instruction == "do()":
                flag = True
            elif flag:
                nums = instruction[4:-1].split(",")
                result += int(nums[0]) * int(nums[1])

    except FileNotFoundError:
        print("The file 'input.txt' was not found.")
    return result

if __name__ == '__main__':  
    result = main()
    print(f"The total of the multiplications is: {result}")
