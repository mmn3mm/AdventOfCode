target_file = "input.txt"


def read_data(targetfile):
    moves = []
    with open(targetfile) as f:
        raw = f.read()
        raw = raw.split('\n')
        for i in raw:
            move1, move2 = i.split(' ')
            move1 = 2- (ord('C') - ord(move1))
            move2 = 2- (ord('Z') - ord(move2))
            moves.append((move1, move2))
    return moves


# A for Rock, B for Paper, and C for Scissors

if __name__ == '__main__':
    beats = {0: 2, 1: 0, 2: 1}  # key beats value eg: 0 (Rock) beats 2 Scissors
    score = {0: 1, 1: 2, 2: 3}  # values of each
    moves = read_data(target_file)
    score1 = 0
    score2 = 0
    for move in moves:
        if move[0] == move[1]:
            score1 += 3
            score2 += 3
        elif beats[move[0]] == move[1]:  # player 1 won
            score1 += 6
        elif beats[move[1]] == move[0]:  # player 2 won
            score2 += 6
        score1 += score[move[0]]
        score2 += score[move[1]]
    print(score1)
    print(score2)
