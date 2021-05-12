import numpy as np
from numpy.lib.npyio import load


def compare(referencesPaths, toComparePath):
    toCompare = loadMatrix(toComparePath)

    diff = []
    for refPath in referencesPaths:
        ref = loadMatrix(refPath)
        s = sum(sum(ref - toCompare))
        print(s)
        diff.append(s)
    
    low = min(diff)
    i = diff.index(low)
    print(referencesPaths[i],diff)


def loadMatrix(fullpath):
    with open(f'{fullpath}.npy', 'rb') as f:
        return np.load(f)


if __name__ == '__main__':
    # compare(['dutch_matrix', 'english_matrix'],'temp/1620811326.92402_matrix')
    # m = loadMatrix('dutch_matrix')

    m = loadMatrix('dutch2_matrix')
    print(m)

    m = loadMatrix('english2_matrix')
    print(m)