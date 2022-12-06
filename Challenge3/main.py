target_file = "input.txt"


def read_data(targetfile):
    rucksacks = []
    with open(targetfile) as f:
        raw = f.read()
        rucksacks = raw.split('\n')
        rucksacks = [rucksacks[i:i + 3] for i in range(0, len(rucksacks), 3)]
    return rucksacks


if __name__ == '__main__':
    rucksacks = read_data(target_file)
    priority = 0
    for rs1, rs2, rs3 in rucksacks:
        visited1 = {}
        visited2 = {}
        visited3 = {}
        max_length = max(len(rs1), len(rs2), len(rs3))
        for i in range(max_length):
            visited1[i % len(rs1)] = True
            visited2[i % len(rs2)] = True
            visited3[i % len(rs3)] = True
        for j in rs1:
            if j in rs2 and j in rs3:
                element = ord(j)
                break
        if ord('a')<=element<=ord('z'):
            priority+=1+element-ord('a')
        elif ord('A')<=element <=ord('Z'):
            priority+=27+element-ord('A')
    print(priority)
