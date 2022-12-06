target_file = "input.txt"


def get_state(lines):
    stacks=[[] for i in range(9)]
    for line in lines:
        #each character occupies 3 characters or 3 spaces then a space
        characters=[line[i+1] for i in range(0,len(line),4)]
        for j in range(len(stacks)):
            if characters[j] != ' ':
                stacks[j].append(characters[j])
    for j in range(len(stacks)):
        stacks[j]=stacks[j][::-1]
    return stacks

def read_data(targetfile):
    stacks = []
    moves=[]
    with open(targetfile) as f:
        raw = f.read()
        raw = raw.split('\n')
        stacks=get_state(raw[:8])
        raw=raw[10:]
        for line in raw:
            values=line.split(' ')
            move=[values[1],values[3],values[5]]#num,from,to
            move=[int(i) for i in move]
            moves.append(move)
    return stacks,moves



if __name__ == '__main__':
    stacks,moves = read_data(target_file)
    for move in moves:
        num=move[0]
        from_=move[1]-1
        to=move[2]-1
        for i in range(num):

            stacks[to].append(stacks[from_].pop())
        txt=""
    for i in stacks:
        if len(i) >0:
            txt+=i.pop()
    print(txt)