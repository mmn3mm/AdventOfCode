target_file = "input.txt"


def read_data(targetfile):
    stream=""
    with open(targetfile) as f:
        stream = f.read()
    return stream

def check_string(str):
    visited={}
    for i in str:
        if i in visited:
            return False
        visited[i]=True
    return True


if __name__ == '__main__':
    stream = read_data(target_file)
    for i in range(len(stream)-14):
        if check_string(stream[i:i+14]):
            print(i+14)
            break