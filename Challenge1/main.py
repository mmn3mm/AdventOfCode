target_file = "input_1.txt"


def read_data(targetfile):
    elfs = []
    with open(targetfile) as f:
        raw = f.read()
        elfs = raw.split('\n\n')
        elfs = [i.split('\n') for i in elfs]
        elfs = [sum([int(i) for i in j]) for j in elfs]
    return elfs


if __name__ == '__main__':
    elfs_calories = read_data(target_file)
    max_calories = max(elfs_calories)
    # Puzzle 1 solution
    print(max_calories)
    max_n_calories = 0
    n = 3
    for i in range(n):
        max_calories = max(elfs_calories)
        elfs_calories.remove(max_calories)
        max_n_calories += max_calories
    print(max_n_calories)
    # Puzzle 2 solution
