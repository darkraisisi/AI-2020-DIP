import sys
import time
import numpy as np
from math import ceil
from tempfile import TemporaryFile


def reduce(lines):
    current_word = None
    word = None
    coordl1, coordl2 = 0, 0
    matrix = np.zeros((28,28),dtype=int)
    for line in lines:
        # remove leading and trailing whitespace
        line = line.strip()

        # parse the input we got from mapper.py
        word, count = line.split('\t', 1)
        # convert count (currently a string) to int
        try:
            count = int(count)
        except ValueError:
            # count was not a number, so silently
            # ignore/discard this line
            pass

        # this IF-switch only works because Hadoop sorts map output
        # by key (here: word) before it is passed to the reducer
        
        if current_word == word:
            matrix[coordl1][coordl2] += count
        else:
            try:
                l1, l2 = list(word)
            except ValueError:
                print('error', word)

            unil1, unil2 = ord(l1), ord(l2)
            # a-z gets 0-25 punctuation and spaces 26 everything else 27
            coordl1 = unil1 - 97 if unil1 >= 97 and unil1 <= 122 else 26 if unil1 < 97 else 27
            coordl2 = unil2 - 97 if unil2 >= 97 and unil2 <= 122 else 26 if unil2 < 97 else 27
            current_word = word
            matrix[coordl1][coordl2] += count

    return matrix


def saveMatrix(matrix, name, norm=False):
    if norm:
        matrix = zScore(matrix)
    with open(f'temp/{name}_matrix.npy', 'wb') as f:
        np.save(f, matrix)


def zScore(matrix):
    mu = np.mean(matrix)
    std = np.std(matrix)
    print(f'mu:{mu}, std:{std}')
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            matrix[row][col] = ceil((matrix[row][col] - mu) / std) # Zscore
            # matrix[row][col] = ceil(matrix[row][col] / mu) # mean

    return matrix

if __name__ == "__main__":
    # input comes from STDIN
    try:
        name = sys.argv[1]
    except IndexError:
        name = 'temp'

    print(name)
    saveMatrix(reduce(sys.stdin), name, norm=False)       