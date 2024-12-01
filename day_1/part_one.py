
def insert_sorted(arr, element):
    if len(arr) == 0:
        arr.append(element)
    else:
        for i in range(len(arr)):
            if element < arr[i]:
                arr.insert(i, element)
                break
        else:
            arr.append(element)

def main():
    total_difference = 0
    try:
        with open('day_1/input.txt', 'r') as f:
            lines = f.readlines()
            
            left, right = [], []
            for line in lines:
                elements = line.split()
                insert_sorted(left, elements[0])
                insert_sorted(right, elements[1])
            
            total_difference = sum(abs(int(left[i]) - int(right[i])) for i in range(len(left)))
                
    except FileNotFoundError:
        print("The file 'input.txt' was not found.")
    return total_difference

if __name__ == '__main__':
    total_distance = main()
    print(f"The total distance is {total_distance}")