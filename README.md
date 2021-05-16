# AI-2020-DIP
2020 Hogeschool Utrecht 2020 Course on Distributed Processing.


# Assignment 2, MapReduce:
Run the full assignment `./setup.sh` in the folder `MapReduce`

## Initialisation :
`python mapper.py < english.txt | sort -k1,1| python reducer.py english`

`python mapper.py < dutch.txt | sort -k1,1| python reducer.py dutch`

## Mapper:
Here you can alter what char's will be converted to a standerd _

## Reducer:
The reducer will return and save a matrix of counted letter combinations.
Also normalizes the matrix, default can be changed.

## Comparer/ validation:
`python main.py validation.txt`

## main:
This python files ties everything together, just in a way to show it can be done without unreadable commands.
This file will print a  prediction per result and a final score per language.

# Analysis:
Normalizing the data really helped in filtering out actual patterns, here you can see the mean and the standard deviation.
This will be printed to the shell when running the setup/main.

english:
mu:123.70, std:339.93

dutch:
mu:127.85, std:359.16

The final line will be the results.
Here you can see that there is a high accuracy.
The actual 73 dutch and 119 (including newlines and sources lines...) isn't that far of from my predicted data.
{'english_matrix': 116, 'dutch_matrix': 75}