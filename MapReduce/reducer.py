import sys
import numpy as np

current_word = None
word = None

matrix = np.zeros((27,27),dtype=int)

# input comes from STDIN
for line in sys.stdin:
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
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    
    if current_word == word:
        matrix[coordl1][coordl2] += count
    else:
        if current_word:
            # write result to STDOUT
            # print(f'{current_word}\t{current_count}')
            print(l1, coordl1, l2, coordl2)
        try:
            l1, l2 = list(word)
        except ValueError:
            continue

        coordl1 = ord(l1) - 97 if ord(l1) >= 97 else 26
        coordl2 = ord(l2) - 97 if ord(l2) >= 97 else 26
        current_word = word
        matrix[coordl1][coordl2] += count

print(matrix)