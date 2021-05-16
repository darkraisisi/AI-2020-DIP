import sys
import os
import mapper
import reducer
import compare

name = sys.argv[1]
languageHits = {}

def addLanguage(name, obj):
    if name in obj:
        obj[name] += 1
    else:
        obj[name] = 1

    return obj


with open(name,'r') as f:
    line = f.readline()
    
    while line:
        if line != '\n':
            ret = mapper.filter(line, inline=False)
            ret.sort()
            reducer.saveMatrix(reducer.reduce(ret), 'temp')
            lang = compare.compare(['dutch_matrix', 'english_matrix'], 'temp_matrix') # ZScore normalized.
            addLanguage(lang, languageHits)
        line = f.readline()

    print(languageHits)
    os.remove('temp_matrix.npy')
