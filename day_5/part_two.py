from collections import defaultdict, deque

def parse_input(input_text):
    rules_section, updates_section = input_text.strip().split("\n\n")
    rules = []
    for line in rules_section.splitlines():
        x, y = map(int, line.split('|'))
        rules.append((x, y))
    updates = []
    for line in updates_section.splitlines():
        update = list(map(int, line.split(',')))
        updates.append(update)
    return rules, updates

def is_valid_update(update, rules):
    position_map = {page: idx for idx, page in enumerate(update)}
    for x, y in rules:
        if x in position_map and y in position_map:
            if position_map[x] > position_map[y]:
                return False
    return True

def reorder_update(update, rules):
    graph = defaultdict(list)
    indegree = defaultdict(int)
    all_pages = set(update)
    
    for x, y in rules:
        if x in all_pages and y in all_pages:
            graph[x].append(y)
            indegree[y] += 1
            if x not in indegree:
                indegree[x] = 0
    
    queue = deque([node for node in update if indegree[node] == 0])
    sorted_update = []
    
    while queue:
        current = queue.popleft()
        sorted_update.append(current)
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_update

def middle_page_number(update):
    mid_index = len(update) // 2
    return update[mid_index]

def main(input_text):
    rules, updates = parse_input(input_text)
    total_middle_sum = 0
    
    for update in updates:
        if not is_valid_update(update, rules):
            reordered_update = reorder_update(update, rules)
            total_middle_sum += middle_page_number(reordered_update)
    
    return total_middle_sum

if __name__ == "__main__":
    try:
        with open("day_5/input.txt", "r") as file:
            input_text = file.read()
            total_middle_sum = main(input_text)
            print(f"The total sum of middle page numbers is {total_middle_sum}")
    except FileNotFoundError:
        print("input.txt not found")
