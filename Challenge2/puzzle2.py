target_file = "input.txt"

beats = {0: 2, 1: 0, 2: 1}  # key beats value eg: 0 (Rock) beats 2 Scissors
score = {0: 1, 1: 2, 2: 3}  # values of each
loses= {2:0,0:1,1:2}

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


def calculate_score(moves):
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
    return score1,score2




def get_correct_moves(moves):
    WIN,LOSE,DRAW=2,0,1
    correct_moves=[]
    for move,condition in moves:
        if condition==WIN:
            my_move=loses[move]
        elif condition==LOSE:
            my_move=beats[move]
        else:
            my_move=move
        correct_moves.append((move,my_move))
    return correct_moves

# A for Rock, B for Paper, and C for Scissors



if __name__ == '__main__':
    moves = read_data(target_file)
    correct_moves=get_correct_moves(moves)
    score1,score2=calculate_score(correct_moves)
    print(score1,score2)
