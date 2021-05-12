import sys

punctuation = [
    ' ', '.', ',', '?', '!', ':', ';', '-', '\'', '\"', '’', '“',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
]

def filter(line, inline=True):
    ret = []
    filterd = line.strip().lower()
    for p in punctuation:
        filterd = filterd.replace(p, '_')

    words = [filterd[i:i+2] for i in range(0, len(filterd)-1, 1)]
    for word in words:
        if inline:
            print(f'{word}\t{1}')
        else:
            ret.append(f'{word}\t{1}')

    return ret


if __name__ == '__main__':
    for line in sys.stdin:
        filter(line)