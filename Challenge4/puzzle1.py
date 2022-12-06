target_file = "input.txt"


def read_data(targetfile):
    intervals = []
    with open(targetfile) as f:
        raw = f.read()
        checks = raw.split('\n')
        checks = [i.split(',') for i in checks]
        for i in checks:
            interval1=[int(j) for j in i[0].split('-')]
            interval2=[int(j) for j in i[1].split('-')]
            intervals.append((interval1,interval2))
    return intervals


if __name__ == '__main__':
    intervals = read_data(target_file)
    pairs=0
    for interval in intervals:
        sections1,sections2=interval
        if sections1[0] <= sections2[0] and sections1[1]>=sections2[1]:
            pairs+=1
        elif sections1[0] >= sections2[0] and sections1[1]<=sections2[1]:
            pairs+=1
    print(pairs)