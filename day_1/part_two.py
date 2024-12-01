def main():
    total_similarity = 0
    try:
        with open('day_1/input.txt', 'r') as f:
            lines = f.readlines()
            
            left, right = [], []
            for line in lines:
                elements = line.split()
                left.append(elements[0])
                right.append(elements[1])
            
            total_similarity = sum(int(left[i]) * right.count(left[i]) for i in range(len(left)))
                
    except FileNotFoundError:
        print("The file 'input.txt' was not found.")
    return total_similarity

if __name__ == '__main__':
    total_similarity = main()
    print(f"The total similarity is {total_similarity}")