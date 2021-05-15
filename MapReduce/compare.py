import numpy as np


def compare(referencesPaths, toComparePath):
    toCompare = loadMatrix(toComparePath)

    diffs = []
    for refPath in referencesPaths:
        ref = loadMatrix(refPath)
        total = sum(sum(ref))
        sub = sum(sum(abs(ref - toCompare)))
        diff = total - sub
        diffs.append(diff)
    
    high = max(diffs)
    i = diffs.index(high)
    print(referencesPaths[i],diffs)
    return referencesPaths[i]


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