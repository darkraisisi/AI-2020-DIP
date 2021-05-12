import sys

from numpy.core.fromnumeric import sort
import mapper
import reducer
import compare

name = sys.argv[1]

with open(name,'r') as f:
    line = f.readline()
    
    while line:
        if line != '\n':
            ret = mapper.filter(line, inline=False)
            ret.sort()
            reducer.saveMatrix(reducer.reduce(ret),'temp')
            compare.compare(['dutch2_matrix', 'english2_matrix'], 'temp/temp_matrix')
        line = f.readline()